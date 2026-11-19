# Aviation Weather Dashboard

A Django-based web application that retrieves and displays aviation weather information for airports using their ICAO codes.

The application integrates the Aviation Weather API to retrieve METAR observations and TAF forecasts and presents the information through a Bootstrap dashboard.

## 1. Project Overview

The main objective is to build an Aviation Weather Dashboard that allows users to search for an airport using its ICAO code and view its current weather conditions and forecast information.

### Implemented Features

- Django project setup.
- Integration with AviationWeather.gov API.
- METAR data retrieval.
- TAF data retrieval.
- Airport search using ICAO codes.
- Dynamic weather dashboard.
- Bootstrap 5 responsive interface.
- Weather information cards.
- Raw METAR report display.
- TAF forecast information.
- TAF forecast period cards.
- Error handling for API requests.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| HTML5 | Webpage structure |
| CSS3 | Custom styling |
| Bootstrap 5 | Responsive dashboard design |
| Bootstrap Icons | Weather and aviation icons |
| Requests | API communication |
| AviationWeather.gov | Aviation weather data source |

## 3. Project Structure

```text
aviation_weather/
│
├── manage.py
│
├── aviation_weather/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── weather/
│   ├── migrations/
│   ├── templates/
│   │   └── weather/
│   │       └── dashboard.html
│   │
│   ├── services.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── .gitignore
└── README.md
```

*Note: This is the documented project structure based on our current implementation. Adjust it if your actual folders differ.*

## 4. API Integration

Data is retrieved from AviationWeather.gov.

### METAR API

Endpoint:

```text
https://aviationweather.gov/api/data/metar
```

Purpose:
- Retrieve current airport weather observations.
- Retrieve temperature and dew point.
- Retrieve wind direction and speed.
- Retrieve visibility.
- Retrieve raw METAR report.

### TAF API

Endpoint:

```text
https://aviationweather.gov/api/data/taf
```

Purpose:
- Retrieve airport weather forecasts.
- Retrieve forecast validity periods.
- Retrieve wind information.
- Retrieve visibility information.
- Retrieve weather and cloud information.
- Retrieve raw TAF report.

Both APIs receive the airport ICAO code as a parameter and return JSON data.

## 5. Backend Implementation

### services.py

Two functions have been implemented:

**get_metar(icao_code)**

Fetches METAR information for the selected airport.

**get_taf(icao_code)**

Fetches TAF forecast information for the selected airport.

The Requests library is used to communicate with the external API.

### views.py

The dashboard view performs the following operations:

1. Receives the ICAO code from the GET request.
2. Uses VOBL as the default airport.
3. Converts the ICAO code to uppercase.
4. Calls the METAR function.
5. Calls the TAF function.
6. Handles API request errors separately.
7. Sends weather information to the dashboard template.

Template context variables:

```python
{
    "weather": weather,
    "taf": taf,
    "error": error,
    "taf_error": taf_error,
}
```

## 6. Frontend Implementation

The dashboard is developed using Django templates and Bootstrap 5.

### Dashboard Components

**A. Airport Search**

Users can enter a four-character ICAO code to retrieve airport weather information.

**B. METAR Dashboard**

Displays:
- Airport name and ICAO code.
- Temperature.
- Dew point.
- Wind direction.
- Wind speed.
- Visibility.
- Raw METAR report.

**C. TAF Forecast Section**

Displays:
- Airport identification.
- Forecast issue time.
- Forecast validity.
- Forecast periods.
- Wind information.
- Visibility.
- Weather conditions.
- Cloud information.
- Raw TAF report.

**D. Responsive UI**

Bootstrap cards, grid layouts, icons, navigation bar, alerts and custom CSS are used to create an attractive dashboard.

## 7. How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate into the project

```bash
cd aviation_weather
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install django requests
```

### Step 6: Apply migrations

```bash
python manage.py migrate
```

### Step 7: Run the server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 8. Test Airports

The following ICAO codes can be used for testing:

| ICAO | Airport |
|---|---|
| VOBL | Bengaluru |
| VIDP | Delhi |
| VOHS | Hyderabad |
| VOMM | Chennai |
| VABB | Mumbai |

Availability of METAR and TAF reports depends on the airport and the API data.

## 9. Current Project Status

| Feature | Status |
|---|---|
| Django setup | Completed |
| API integration | Completed |
| METAR retrieval | Completed |
| Dashboard design | Completed |
| ICAO search | Completed |
| TAF retrieval | Completed |
| TAF dashboard display | Implemented |
| TAF timeline | Added; visual change needs verification |

## 10. Future Enhancements

The following features are planned:

1. Improve TAF forecast timeline visualization.
2. Weather condition classification.
3. Weather alerts for important aviation conditions.
4. Database integration.
5. Airport search history.
6. Improved forecast presentation.
7. Final testing and deployment.

## 11. Project Objective

The final goal is to develop a complete Aviation Weather Dashboard that provides airport weather observations, forecasts and useful aviation weather information through a user-friendly web application.

**Project Status:** Development in Progress.