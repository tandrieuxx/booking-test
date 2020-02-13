{% block javascript %}
<script>
    // Handle resource form
    const resourceForm = $("#resource-modal form");
    resourceForm.submit(e => {
        // Prevent reloading the page
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "{% url 'resource' %}",
            data: resourceForm.serialize(),
            success: response => {
                // Append the new resource component to the list
                $("#resource-list").append(response);
                $("#resource-modal").modal("hide");
                resourceForm.trigger("reset");
            },
            error: response => {
                console.log(response);
            }
        });
    });

    // Handle booking form
    const bookingForm = $("#booking-modal form");
    bookingForm.submit(e => {
        // Prevent reloading the page
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: "{% url 'booking' %}",
            data: bookingForm.serialize(),
            success: response => {
                // Append the new booking component to the list
                $("#booking-list").append(response);
                $("#booking-modal").modal("hide");
                bookingForm.trigger("reset");
            },
            error: response => {
                console.log(response);
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
</script>
{% endblock javascript %}