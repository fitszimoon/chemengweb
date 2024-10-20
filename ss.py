from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ethanol As Gas</title>
        <style>
            /* General CSS styles */
            body {
                margin: 0;
                padding: 0;
                font-family: 'Montserrat', sans-serif;
                color: black;
                height: 100vh;
                overflow: hidden;
                display: flex;
                transition: background-image 0.3s ease;
            }

            /* Video Background */
            #video-background {
                position: fixed;
                top: 0;
                left: 0;
                min-width: 100%;
                min-height: 100%;
                z-index: -2; /* Behind everything else */
                object-fit: cover; /* Ensures the video covers the entire viewport */
                filter: brightness(50%); /* Optional: Darkens the video for better text contrast */
            }

            /* Overlay for additional background */
            .background-overlay {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: -1; /* Keep it behind the content */
                background-size: cover;
                background-position: center;
                opacity: 0;
                transition: opacity 0.3s ease;
            }

            .main-content {
                flex-grow: 1;
                padding: 20px;
                overflow: auto;
                z-index: 1; /* Ensure content is above the background */
            }

            header {
                background-color: rgba(227, 0, 11, 0.8); /* Semi-transparent header */
                padding: 20px;
                text-align: center;
            }

            header h1 {
                font-size: 2.5rem;
                color: white;
                text-transform: uppercase;
            }

            .intro {
                text-align: center;
                padding: 50px 20px;
            }

            .intro h2 {
                font-size: 2rem;
                color: #e3000b;
                text-transform: uppercase;
                animation: flicker 1.5s infinite;
            }

            .intro p {
                font-size: 1.2rem;
                color: black;
            }

            .cards {
                display: flex;
                justify-content: center;
                padding: 20px;
            }

            .card {
                background-color: white;
                color: black;
                margin: 10px;
                padding: 20px;
                width: 200px;
                text-align: center;
                border: 5px solid #e3000b;
                box-shadow: 10px 10px 0 black;
                transition: transform 0.3s ease-in-out;
                cursor: pointer;
            }

            .card:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            footer {
                background-color: #e3000b;
                text-align: center;
                padding: 100px 30px 500px;
            }

            footer p {
                margin: 0;
                color: white;
            }

            /* Sidebar */
            .sidebar {
                background-color: #1e1e1e;
                width: 250px;
                height: 100%;
                position: fixed;
                top: 0;
                left: -250px;
                transition: left 0.3s;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                z-index: 1000;
            }

            .sidebar a {
                color: white;
                text-decoration: none;
                display: block;
                margin: 15px 0;
                font-size: 1.2rem;
                text-align: center;
                transition: transform 0.3s ease-in-out;
            }

            .sidebar a:hover {
                color: #e3000b;
                transform: scale(1.1) rotate(-3deg);
            }

            .sidebar.open {
                left: 0;
            }

            .toggle-btn {
                position: absolute;
                top: 20px;
                left: 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 1.2rem;
                cursor: pointer;
                z-index: 1100;
                transition: transform 0.3s ease-in-out;
            }

            .toggle-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            .main-content.shifted {
                margin-left: 250px;
            }

            header.shifted {
                margin-left: 250px;
            }

            @keyframes flicker {
                0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {
                    opacity: 1;
                }
                20%, 24%, 55% {
                    opacity: 0;
                }
            }
        </style>
    </head>
    <body>
        <!-- Video Background -->
        <video autoplay muted loop id="video-background">
            <source src="/static/background-video.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

        <!-- Toggle Button for Sidebar -->
        <button class="toggle-btn" onclick="toggleSidebar()">☰ Menu</button>

        <!-- Sidebar Section -->
        <div class="sidebar" id="sidebar">
            <a href="/">Home</a>
            <a href="#">About</a>
            <a href="#">Gallery</a>
            <a href="#">Contact</a>
        </div>

        <!-- Overlay for background image -->
        <div class="background-overlay" id="background-overlay"></div>

        <!-- Main Content -->
        <div class="main-content" id="main-content">
            <header id="header">
                <div class="logo">
                    <h1>Ethanol As Gas</h1>
                </div>
            </header>

            <main>
                <section class="intro">
                    <h2>Steal Your Heart</h2>
                    <p>Welcome to the Phantom Thieves' secret lair. We’re here to change hearts and reform society!</p>
                </section>
                <section class="cards">
                    <a href="/joker" class="card" onmouseover="changeBackground('/static/url1.jpg')" onmouseout="resetBackground()">
                        <h3>Lesson</h3>
                        <p>Information about Ethanol.</p>
                    </a>
                    <a href="/morgana2" class="card" onmouseover="changeBackground('/static/url2.jpg')" onmouseout="resetBackground()">
                        <h3>Quiz</h3>
                        <p>Test your knowledge.</p>
                    </a>
                    <div class="card" onmouseover="changeBackground('/static/url3.jpg')" onmouseout="resetBackground()">
                        <h3>Le creators</h3>
                        <p>Group members and Professor.</p>
                    </div>
                </section>
            </main>

            <footer>
                <p>&copy; 2024 Phantom Thieves. All Rights Reserved.</p>
            </footer>
        </div>

        <script>
            // Sidebar toggle function
            function toggleSidebar() {
                var sidebar = document.getElementById('sidebar');
                var mainContent = document.getElementById('main-content');
                sidebar.classList.toggle('open');
                mainContent.classList.toggle('shifted');
                document.getElementById('header').classList.toggle('shifted');
            }

            function changeBackground(imageUrl) {
                const overlay = document.getElementById('background-overlay');
                overlay.style.backgroundImage = `url(${imageUrl})`;
                overlay.style.opacity = 1;
            }

            function resetBackground() {
                const overlay = document.getElementById('background-overlay');
                overlay.style.opacity = 0;
            }
        </script>
    </body>
    </html>
    '''


@app.route('/joker')
def joker_info():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Joker Info</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Montserrat', sans-serif;
                color: black; /* Changed text color to black */
                height: 100vh;
                overflow: hidden;
                display: flex;
            }

            /* Same styles as home page for consistency */
            body::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(270deg, #e3000b, #ffdd00, #000000, #ffffff);
                background-size: 800% 800%;
                animation: gradient 10s ease infinite;
                z-index: -1;
            }

            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .main-content {
                flex-grow: 1;
                padding: 20px;
                overflow: auto;
                transition: margin-left 0.3s;
                z-index: 1; /* Ensure content is above the background */
            }

            header {
                background-color: rgba(227, 0, 11, 0.8); /* Semi-transparent header */
                padding: 20px;
                text-align: center;
                transition: margin-left 0.3s;
            }

            header h1 {
                font-size: 2.5rem;
                color: white;
                text-transform: uppercase;
            }

            .info-page {
                display: flex; /* Center content vertically */
                flex-direction: column; /* Stack elements vertically */
                justify-content: center; /* Center content vertically */
                align-items: center; /* Center content horizontally */
                text-align: center;
                padding: 50px 20px;
                z-index: 1; /* Ensure content is above the background */
                height: 100%; /* Ensure it takes full height */
            }

            .next-btn, .back-btn {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                font-size: 1.5rem; /* Increased font size */
                cursor: pointer;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .next-btn:hover, .back-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Sidebar */
            .sidebar {
                background-color: #1e1e1e;
                width: 250px;
                height: 100%;
                position: fixed;
                top: 0;
                left: -250px;
                transition: left 0.3s;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                z-index: 1000; /* Ensure sidebar is above other content */
            }

            .sidebar a {
                color: white;
                text-decoration: none;
                display: block;
                margin: 15px 0;
                font-size: 1.2rem;
                text-align: center;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            .sidebar a:hover {
                color: #e3000b;
                transform: scale(1.1) rotate(-3deg); /* Animation on hover */
            }

            /* Sidebar open state */
            .sidebar.open {
                left: 0;
            }

            /* Button to open/close sidebar */
            .toggle-btn {
                position: absolute;
                top: 20px;
                left: 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 1.2rem;
                cursor: pointer;
                z-index: 1100; /* Ensure button is above the sidebar */
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .toggle-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Adjust main content and header when sidebar is open */
            .main-content.shifted {
                margin-left: 250px;
            }

            header.shifted {
                margin-left: 250px;
            }

        </style>
    </head>
    <body>
        <!-- Toggle Button for Sidebar -->
        <button class="toggle-btn" onclick="toggleSidebar()">☰ Menu</button>

        <!-- Sidebar Section -->
        <div class="sidebar" id="sidebar">
            <a href="/">Home</a>
            <a href="#">About</a>
            <a href="#">Gallery</a>
            <a href="#">Contact</a>
        </div>

        <!-- Main Content -->
        <div class="main-content" id="main-content">
            <header id="header">
                <div class="logo">
                    <h1>Input title</h1>
                </div>
            </header>

            <div class="info-page">
                <h2>Input subtitle</h2>
                <p>Input text.</p>
                <p>Input text.</p>
                <button class="next-btn" onclick="window.location.href='/morgana'">Next: Morgana</button>
                <button class="back-btn" onclick="window.location.href='/'">Home</button>
            </div>
        </div>

        <script>
            // Sidebar toggle function
            function toggleSidebar() {
                var sidebar = document.getElementById('sidebar');
                var mainContent = document.getElementById('main-content');
                sidebar.classList.toggle('open');
                mainContent.classList.toggle('shifted');
                document.getElementById('header').classList.toggle('shifted');
            }
        </script>
    </body>
    </html>
    '''

@app.route('/morgana')
def morgana_info():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Morgana Info</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Montserrat', sans-serif;
                color: black; /* Changed text color to black */
                height: 100vh;
                overflow: hidden;
                display: flex;
            }

            /* Same styles as home page for consistency */
            body::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(270deg, #e3000b, #ffdd00, #000000, #ffffff);
                background-size: 800% 800%;
                animation: gradient 10s ease infinite;
                z-index: -1;
            }

            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .main-content {
                flex-grow: 1;
                padding: 20px;
                overflow: auto;
                transition: margin-left 0.3s;
                z-index: 1; /* Ensure content is above the background */
            }

            header {
                background-color: rgba(227, 0, 11, 0.8); /* Semi-transparent header */
                padding: 20px;
                text-align: center;
                transition: margin-left 0.3s;
            }

            header h1 {
                font-size: 2.5rem;
                color: white;
                text-transform: uppercase;
            }

            .info-page {
                display: flex; /* Center content vertically */
                flex-direction: column; /* Stack elements vertically */
                justify-content: center; /* Center content vertically */
                align-items: center; /* Center content horizontally */
                text-align: center;
                padding: 50px 20px;
                z-index: 1; /* Ensure content is above the background */
                height: 100%; /* Ensure it takes full height */
            }

            .next-btn, .back-btn {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                font-size: 1.5rem; /* Increased font size */
                cursor: pointer;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .next-btn:hover, .back-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Sidebar */
            .sidebar {
                background-color: #1e1e1e;
                width: 250px;
                height: 100%;
                position: fixed;
                top: 0;
                left: -250px;
                transition: left 0.3s;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                z-index: 1000; /* Ensure sidebar is above other content */
            }

            .sidebar a {
                color: white;
                text-decoration: none;
                display: block;
                margin: 15px 0;
                font-size: 1.2rem;
                text-align: center;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            .sidebar a:hover {
                color: #e3000b;
                transform: scale(1.1) rotate(-3deg); /* Animation on hover */
            }

            /* Sidebar open state */
            .sidebar.open {
                left: 0;
            }

            /* Button to open/close sidebar */
            .toggle-btn {
                position: absolute;
                top: 20px;
                left: 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 1.2rem;
                cursor: pointer;
                z-index: 1100; /* Ensure button is above the sidebar */
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .toggle-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Adjust main content and header when sidebar is open */
            .main-content.shifted {
                margin-left: 250px;
            }

            header.shifted {
                margin-left: 250px;
            }

            /* Sample card styles */
            .card {
                background-color: #f0f0f0;
                border-radius: 8px;
                padding: 20px;
                margin: 20px;
                cursor: pointer;
                transition: transform 0.2s;
            }

            .card:hover {
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <!-- Toggle Button for Sidebar -->
        <button class="toggle-btn" onclick="toggleSidebar()">☰ Menu</button>

        <!-- Sidebar Section -->
        <div class="sidebar" id="sidebar">
            <a href="/">Home</a>
            <a href="#">About</a>
            <a href="#">Gallery</a>
            <a href="#">Contact</a>
        </div>

        <!-- Main Content -->
        <div class="main-content" id="main-content">
            <header id="header">
                <div class="logo">
                    <h1>Input title</h1>
                </div>
            </header>

            <div class="info-page">
                <h2>Input subtitle</h2>
                <p>input text.</p>
                <p>input text.</p>
                <button class="next-btn" onclick="window.location.href='/joker'">Previous: Joker</button>
                <button class="back-btn" onclick="window.history.back()">Back</button>
            </div>

            <!-- Sample Morgana Card -->
            <div class="card morgana-card" onclick="preventRedirect(event)">
                <h3>Morgana Card</h3>
                <p>This card does not redirect anywhere!</p>
            </div>
        </div>

        <script>
            // Sidebar toggle function
            function toggleSidebar() {
                var sidebar = document.getElementById('sidebar');
                var mainContent = document.getElementById('main-content');
                sidebar.classList.toggle('open');
                mainContent.classList.toggle('shifted');
                document.getElementById('header').classList.toggle('shifted');
            }

            // Prevent redirect function
            function preventRedirect(event) {
                event.stopPropagation();
                alert("This card does not redirect anywhere.");
            }
        </script>
    </body>
    </html>
    '''

@app.route('/morgana2')
def morgana2_info():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Joker Info</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Montserrat', sans-serif;
                color: black; /* Changed text color to black */
                height: 100vh;
                overflow: hidden;
                display: flex;
            }

            /* Same styles as home page for consistency */
            body::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: linear-gradient(270deg, #e3000b, #ffdd00, #000000, #ffffff);
                background-size: 800% 800%;
                animation: gradient 10s ease infinite;
                z-index: -1;
            }

            @keyframes gradient {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .main-content {
                flex-grow: 1;
                padding: 20px;
                overflow: auto;
                transition: margin-left 0.3s;
                z-index: 1; /* Ensure content is above the background */
            }

            header {
                background-color: rgba(227, 0, 11, 0.8); /* Semi-transparent header */
                padding: 20px;
                text-align: center;
                transition: margin-left 0.3s;
            }

            header h1 {
                font-size: 2.5rem;
                color: white;
                text-transform: uppercase;
            }

            .info-page {
                display: flex; /* Center content vertically */
                flex-direction: column; /* Stack elements vertically */
                justify-content: center; /* Center content vertically */
                align-items: center; /* Center content horizontally */
                text-align: center;
                padding: 50px 20px;
                z-index: 1; /* Ensure content is above the background */
                height: 100%; /* Ensure it takes full height */
            }

            .next-btn, .back-btn {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                font-size: 1.5rem; /* Increased font size */
                cursor: pointer;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .next-btn:hover, .back-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Sidebar */
            .sidebar {
                background-color: #1e1e1e;
                width: 250px;
                height: 100%;
                position: fixed;
                top: 0;
                left: -250px;
                transition: left 0.3s;
                padding: 20px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                z-index: 1000; /* Ensure sidebar is above other content */
            }

            .sidebar a {
                color: white;
                text-decoration: none;
                display: block;
                margin: 15px 0;
                font-size: 1.2rem;
                text-align: center;
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            .sidebar a:hover {
                color: #e3000b;
                transform: scale(1.1) rotate(-3deg); /* Animation on hover */
            }

            /* Sidebar open state */
            .sidebar.open {
                left: 0;
            }

            /* Button to open/close sidebar */
            .toggle-btn {
                position: absolute;
                top: 20px;
                left: 20px;
                background-color: #e3000b;
                color: white;
                border: none;
                padding: 10px 15px;
                font-size: 1.2rem;
                cursor: pointer;
                z-index: 1100; /* Ensure button is above the sidebar */
                transition: transform 0.3s ease-in-out; /* Animation effect */
            }

            /* Animation on hover */
            .toggle-btn:hover {
                transform: scale(1.1) rotate(-3deg);
            }

            /* Adjust main content and header when sidebar is open */
            .main-content.shifted {
                margin-left: 250px;
            }

            header.shifted {
                margin-left: 250px;
            }

        </style>
    </head>
    <body>
        <!-- Toggle Button for Sidebar -->
        <button class="toggle-btn" onclick="toggleSidebar()">☰ Menu</button>

        <!-- Sidebar Section -->
        <div class="sidebar" id="sidebar">
            <a href="/">Home</a>
            <a href="#">About</a>
            <a href="#">Gallery</a>
            <a href="#">Contact</a>
        </div>

        <!-- Main Content -->
        <div class="main-content" id="main-content">
            <header id="header">
                <div class="logo">
                    <h1>Input Title</h1>
                </div>
            </header>

            <div class="info-page">
                <h2>Input subtitle</h2>
                <p>Input text here.</p>
                <p>Input text here.</p>
                <button class="next-btn" onclick="window.location.href='/morgana3'">Next: Morgana3</button>
                <button class="back-btn" onclick="window.location.href='/'">Home</button>
            </div>
        </div>

        <script>
            // Sidebar toggle function
            function toggleSidebar() {
                var sidebar = document.getElementById('sidebar');
                var mainContent = document.getElementById('main-content');
                sidebar.classList.toggle('open');
                mainContent.classList.toggle('shifted');
                document.getElementById('header').classList.toggle('shifted');
            }
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)

