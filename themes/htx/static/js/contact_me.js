$(function() {

    $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            // Prevent spam click and default submit behaviour
            $("#btnSubmit").attr("disabled", true);
            $("#btnSubmit").html("Đang gửi ...");
            event.preventDefault();

            // get values from FORM
            var name = $("input#name").val();
            var email = $("input#email").val();
            var phone = $("input#phone").val();
            var message = $("textarea#message").val();
            var firstName = name; // For Success/Failure Message
            // Check for white space in name for Success/Fail message
            if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }
            $.ajax({
                url: "http://formspree.io/htxcoder@googlegroups.com",
                type: "POST",
                data: {
                    name: name,
                    phone: phone,
                    email: email,
                    message: message
                },
                cache: false,
                success: function() {
                    // Enable button & show success message
                    $("#btnSubmit").attr("disabled", false);
                    $('#success').html("<div class='alert alert-success'>");
                    $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-success')
                        .append("<strong>Cảm ơn. Chúng thôi sẽ phản hồi lại sớm thôi. </strong>");
                    $('#success > .alert-success')
                        .append('</div>');

                    //clear all fields
                    $('#contactForm').trigger("reset");
                    $("#btnSubmit").html("Gửi tin nhắn");
                },
                error: function() {
                    // Fail message
                    $('#success').html("<div class='alert alert-danger'>");
                    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                        .append("</button>");
                    $('#success > .alert-danger').append("<strong>Sorry " + firstName + ", đã có lỗi không mong muốn xảy ra, vui lòng liên hệ trực tiếp với chúng thôi qua email <a href='mailto:htxcoder@googlegroups.com'>htxcoder@googlegroups.com</a>!");
                    $('#success > .alert-danger').append('</div>');
                    //clear all fields
                    $('#contactForm').trigger("reset");
                    $("#btnSubmit").html("Gửi tin nhắn");
                    $("#btnSubmit").attr("disabled", false);
                },
            });
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});

// When clicking on Full hide fail/success boxes
$('#name').focus(function() {
    $('#success').html('');
});
