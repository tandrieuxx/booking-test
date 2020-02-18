{% block javascript %}
<script>
$(() => {
    $(".datetimepicker-input").datetimepicker({
      format: 'DD/MM/YYYY HH:mm',
    });

    const resourceForm = $("#resource-modal form");

    // Prefill resource form for editing
    $("#resource-modal").on("show.bs.modal", e => {
        const id = $(e.relatedTarget).data("id");
        if (id > 0) {
            const resource = $(e.relatedTarget).closest("div.resource");

            // Fill inputs with resource data
            resourceForm.find("input[name='id']").val(id);
            resourceForm.find("input[name='label']").val(resource.find(".resource-label").text());
            const type = resource.find(".resource-type").data("raw-val");
            resourceForm.find("select[name='type'] > option[value='" + type + "']").prop("selected", true);
            resourceForm.find("input[name='location']").val(resource.find(".resource-location").text());
            resourceForm.find("input[name='capacity']").val(resource.find(".resource-capacity").text());
        }
    });


    // Handle resource form
    resourceForm.submit(e => {
        // Prevent reloading the page
        e.preventDefault();

        // Check if ID field is filled to know if it was creation or edition
        const id = resourceForm.find("input[name='id']").val();

        $.ajax({
            type: 'POST',
            url: "{% url 'resource' %}",
            data: resourceForm.serialize(),
            success: response => {
                if(id > 0) {
                    // In case of editing, replace the existing component with the one received
                    $("div.resource[data-id='" + id + "']").replaceWith(response);
                } else {
                    // Otherwise, append the new resource component to the list
                    $("#resource-list").append(response);
                }

                $("#resource-modal").modal("hide");
                resourceForm.trigger("reset");
            },
            error: response => {
                // Replace the form with the received one containing errors
                $("div#resource-form").replaceWith(response.responseText);
            }
        });
    });


    // Prefill booking form for editing
    $("#booking-modal").on("show.bs.modal", e => {
        const id = $(e.relatedTarget).data("id");
        if (id > 0) {
            const booking = $(e.relatedTarget).closest("div.booking");

            // Fill inputs with booking data
            bookingForm.find("input[name='id']").val(id);
            bookingForm.find("input[name='title']").val(booking.find(".booking-title").text());
            bookingForm.find("input[name='start_date']").val(booking.find(".booking-start_date").text());
            bookingForm.find("input[name='end_date']").val(booking.find(".booking-end_date").text());
            const resource = booking.find(".booking-resource").data("raw-val");
            bookingForm.find("select[name='resource'] > option[value='" + resource + "']").prop("selected", true);
        }
    });

    // Handle booking form
    const bookingForm = $("#booking-modal form");
    bookingForm.submit(e => {
        // Prevent reloading the page
        e.preventDefault();

        // Check if ID field is filled to know if it was creation or edition
        const id = bookingForm.find("input[name='id']").val();

        $.ajax({
            type: 'POST',
            url: "{% url 'booking' %}",
            data: bookingForm.serialize(),
            success: response => {
                if(id > 0) {
                    // In case of editing, replace the existing component with the one received
                    $("div.booking[data-id='" + id + "']").replaceWith(response);
                } else {
                    // Append the new booking component to the list
                    $("#booking-list").append(response);
                }

                $("#booking-modal").modal("hide");
                bookingForm.trigger("reset");
            },
            error: response => {
                // Replace the form with the received one containing errors
                $("div#booking-form").replaceWith(response.responseText);
            }
        });
    });

    // Handle resource deletion
    $(".delete-resource").submit(e => {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "{% url 'delete_resource' %}",
            data: $(e.target).serialize(),
            success: response => {
                // Delete the corresponding resource component
                $(e.target).closest(".resource").remove();
            },
            error: response => {
                console.log(response);
            }
        });
    })

    // Handle booking deletion
    $(".delete-booking").submit(e => {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "{% url 'delete_booking' %}",
            data: $(e.target).serialize(),
            success: response => {
                // Delete the corresponding booking component
                $(e.target).closest(".booking").remove();
            },
            error: response => {
                console.log(response);
            }
        });
    })
})
</script>
{% endblock javascript %}