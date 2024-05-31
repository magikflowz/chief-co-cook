import flet as ft

def main(page: ft.Page):
    page.title = "ChefAI - Login"
    
    # Background container with image
    background_container = ft.Container(
        content=None,  # This will be replaced with login or register views
        expand=True,
        image_src="https://c1.wallpaperflare.com/preview/957/1003/725/kitchen-restaurant-restaurant-kitchen-cook.jpg",  # Replace with your image URL
        image_fit=ft.ImageFit.COVER
    )

    # Function to show the login screen
    def show_login(e=None):
        background_container.content = login_view()  # Set the content to the login view
        page.update()  # Update the page to reflect changes

    # Function to show the registration screen
    def show_register(e=None):
        background_container.content = register_view()  # Set the content to the registration view
        page.update()  # Update the page to reflect changes

    # Function to handle login button click
    def login_click(e):
        if username.value == "user" and password.value == "pass":  # Check if credentials are correct (hardcoded for now)
            login_status.value = "Login successful!"  # Display success message
            login_status.color = ft.colors.GREEN  # Set text color to green
        else:
            login_status.value = "Invalid username or password"  # Display error message
            login_status.color = ft.colors.RED  # Set text color to red
        page.update()  # Update the page to reflect changes

    # Function to handle register button click
    def register_click(e):
        # Placeholder for registration logic
        if reg_password.value == reg_confirm_password.value:  # Check if passwords match
            register_status.value = "Registration successful!"  # Display success message
            register_status.color = ft.colors.GREEN  # Set text color to green
        else:
            register_status.value = "Passwords do not match!"  # Display error message
            register_status.color = ft.colors.RED  # Set text color to red
        page.update()  # Update the page to reflect changes

    # Function to create the login view
    def login_view():
        global username, password, login_status  # Declare global variables to store form fields and status message
        
        # Transparent grey background for text fields
        textbox_bgcolor = ft.colors.with_opacity(ft.colors.GREY, 0.5)

        username = ft.TextField(label="Username", width=300)  # Create a text field for username
        password = ft.TextField(label="Password", password=True, width=300)  # Create a text field for password
        login_button = ft.ElevatedButton(text="Login", on_click=login_click)  # Create a login button
        login_status = ft.Text(value="", size=14)  # Create a text element to display the login status
        register_link = ft.TextButton("Register", on_click=show_register)  # Create a link to switch to the registration screen

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Login to ChefAI", size=32, weight="bold"),  # Header text
                    ft.Container(content=username, bgcolor=textbox_bgcolor, border_radius=8),  # Username field with background
                    ft.Container(content=password, bgcolor=textbox_bgcolor, border_radius=8),  # Password field with background
                    login_button,  # Login button
                    login_status,  # Login status message
                    register_link  # Link to registration screen
                ],
                spacing=20,  # Spacing between elements
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Center align elements horizontally
            ),
            alignment=ft.alignment.center,  # Center the container content
            padding=ft.padding.all(20)  # Add some padding around the content
        )

    # Function to create the registration view
    def register_view():
        global reg_username, reg_password, reg_confirm_password, register_status  # Declare global variables to store form fields and status message

        # Transparent grey background for text fields
        textbox_bgcolor = ft.colors.with_opacity(ft.colors.GREY, 0.5)

        reg_username = ft.TextField(label="Username", width=300)  # Create a text field for username
        reg_password = ft.TextField(label="Password", password=True, width=300)  # Create a text field for password
        reg_confirm_password = ft.TextField(label="Confirm Password", password=True, width=300)  # Create a text field for confirming the password
        register_button = ft.ElevatedButton(text="Register", on_click=register_click)  # Create a register button
        register_status = ft.Text(value="", size=14)  # Create a text element to display the registration status
        login_link = ft.TextButton("Back to Login", on_click=show_login)  # Create a link to switch back to the login screen

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("Register for ChefAI", size=32, weight="bold"),  # Header text
                    ft.Container(content=reg_username, bgcolor=textbox_bgcolor, border_radius=8),  # Username field with background
                    ft.Container(content=reg_password, bgcolor=textbox_bgcolor, border_radius=8),  # Password field with background
                    ft.Container(content=reg_confirm_password, bgcolor=textbox_bgcolor, border_radius=8),  # Confirm password field with background
                    register_button,  # Register button
                    register_status,  # Registration status message
                    login_link  # Link to login screen
                ],
                spacing=20,  # Spacing between elements
                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Center align elements horizontally
            ),
            alignment=ft.alignment.center,  # Center the container content
            padding=ft.padding.all(20)  # Add some padding around the content
        )

    # Initially display the login view
    show_login()

    # Add the background and overlay containers to the page
    page.add(background_container)
ft.app(target=main)