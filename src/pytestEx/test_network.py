from playwright.sync_api import Page ,expect , Route, Request
import json

def route_response(response):
    print("Response received:", response.url, response.status)

def route_request_ko_call(route:Route):
    json_data = {"status":"KO"}
    route.fulfill(
    status=200,
    body=json.dumps({"status": "KO"}),
    headers={"content-type": "application/json"}
    )

def add_header_to_XHR(route:Route):
    request = route.request
    if request.resource_type in ["xhr","fetch"]:
        headers = request.headers.copy()
        headers["abc"]="kajjjdjdj"
        route.continue_(headers=headers)
    else:
        route.continue_()


# mocks every response from serer with {"status": "KO"})
# def test_network_events(page: Page):
#     page.route("**/*", route_request_ko_call)  # Event listener for network requests
#      # Event listener for network responses
#     page.goto("https://www.amazon.in")
#     page.get_by_text("MX Player").click()

def test_network_events_request(page: Page):
    page.route("**/*", add_header_to_XHR)  # Event listener for network requests
     # Event listener for network responsesß
    page.goto("https://www.amazon.in")
    page.get_by_text("MX Player").click()
    page.pause()
    
