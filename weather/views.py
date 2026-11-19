
import requests
from django.shortcuts import render

from .services import get_metar, get_taf


def dashboard(request):

    # Get ICAO code
    icao_code = request.GET.get("icao", "VOBL").strip().upper()

    weather = None
    taf = None

    error = None
    taf_error = None

    # Fetch METAR data
    try:
        data = get_metar(icao_code)

        if data:
            weather = data[0]
        else:
            error = f"No METAR information found for {icao_code}"

    except requests.RequestException as e:
        error = f"METAR API error: {e}"

    # Fetch TAF data
    try:
        taf_data = get_taf(icao_code)

        if taf_data:
            taf = taf_data[0]
        else:
            taf_error = f"No TAF information available for {icao_code}"

    except requests.RequestException as e:
        taf_error = f"TAF API error: {e}"

    return render(
        request,
        "weather/dashboard.html",
        {
            "weather": weather,
            "taf": taf,
            "error": error,
            "taf_error": taf_error,
        }
    )
