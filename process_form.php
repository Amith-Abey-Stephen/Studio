
<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve form data
        $fname = $_POST['fname'];
        $lname = $_POST['lname'];
        $email = $_POST['email'];
        $cservice = $_POST['cservice'];
        $message = $_POST['message'];
    
        // Compose email
        $to = "amithabey13@gmail.com"; // Change this to your email address
        $subject = "New Form Submission";
        $body = "First Name: $fname\n";
        $body .= "Last Name: $lname\n";
        $body .= "Email: $email\n";
        $body .= "Service: $cservice\n";
        $body .= "Message:\n$message";
    
        // Send email
        $result = mail($to, $subject, $body);
    
        // Check if email was sent successfully
        if ($result) {
            echo "Thank you for your submission!";
        } else {
            echo "Sorry, there was an error processing your request.";
        }
    } else {
        // If not a POST request, redirect back to the form page
        header("Location: your_form_page.html");
        exit;
    }
    ?>
    