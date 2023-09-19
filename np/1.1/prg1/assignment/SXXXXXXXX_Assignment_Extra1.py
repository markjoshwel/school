"""
Programming 1 Assignment
Mark Joshwel - SXXXXXXXX (IM02/P12) - 12/08/2023
------------------------------------------------
with Extra Feature 1:
    Use real-time carpark available data from data.gov.sg

    Updates Menu Option [3] to ask user if they want to read from a file or
    use real-time carpark available data from data.gov.sg

    Uses:
        urllib.request.urlopen  - To request for data from API
        json.loads              - To parse JSON response
        json.JSONDecodeError    - To handle for JSON parse errors
        datetime.datetime       - To check if data should be refreshed
                                  (provides real-time functionality)

⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄           "what? we can't use
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⠈⠻⣿⣿⣧⠊⠻⣿⣿⣷⡝⢿⣿⣿⣿⣿⣿⣿⣿⣿⡀           standard libary
⠀⢸⣿⣿⣿⣿⣿⣿⡛⣿⣿⡇⠈⠀⠀⠈⠻⣿⣇⠀⢀⠙⠻⢿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣧⡀          modules?"
⠀⢸⣿⣿⣿⣿⣿⣿⠁⢻⣿⡇⠀⠀⠀⠀⠀⠈⠻⣆⠀⠁⠀⠈⠈⠑⠈⢿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⢸⣿⣿⣿⣿⣿⣿⠀⠘⣿⡇⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢼⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠸⣿⣿⣿⣿⢻⡿⠀⠀⠸⡇⠂⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⠒⠉⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣧        "or `import typing`?"
⠀⠀⣿⣿⣿⣿⠀⢧⠀⠀⠁⠁⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⠀⣿⣿⣿⣷⣆⠈⠀⠀⠀⣀⡤⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⢿⣿⣿⣿⣿⣆⠠⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇       "stay together
⠀⠀⢸⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       for the kids..."
⠀⠀⠘⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠆⠠⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾⠟⠋⠁⢀⠔⠀⢸⣿⣿⣿⣿⣿⡿⣿⣿⣿⡇
⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣀⣀⠀⠾⠛⠉⠀⠀⢀⠠⠂⠁⠀⠀⢸⣿⣿⣿⣿⣿⡇⠈⠛⢿⡇
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⢤⠀⠀⠀⠀⢀⣾⣿⣿⣿⡟⣿⠀⠀⠀⠀⠈
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⢠⠂⡆⠀⠀⢀⠎⣿⣿⣿⣿⢡⡏⠀⠀⠀⠀⣠⣴
⠀⠀⠀⠀⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠉⠀⠀⠀⠀⠀⠆⠀⠀⠀⠠⠃⠀⣿⣿⡿⠃⠸⠁⠀⢀⣴⠾⠋⢀
"""

# from typing import Any, Callable  # TODO: comment this out before submission
from urllib.request import urlopen
from json import loads, JSONDecodeError
from datetime import datetime


CSV_CARPARK_INFO: str = "carpark-information.csv"


# --- utility/helper functions --- #


def utils_csv_read(
    file: str, startline: int = 0
) -> tuple[list[dict[str, str | int]], str]:
    """
    utility function to read csv files into dicts in a list
    assumes utf-8 encoding

    arguments
        file: str
            filepath to read from
        startline: int
            line to start from

    returns tuple[list[dict[str, str | int]], str]
        list[dict[str, str | int]]:
            the csv file
        str:
            consumed text if startline > 0
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    csv_data: list[dict[str, str | int]] = []
    prelines: list[str] = []

    with open(file, "r", encoding="utf-8") as csv_fd:
        # consume any lines as given by startline argument
        for _ in range(startline):
            prelines.append(next(csv_fd))

        # attempt to read next line
        try:
            headers = next(csv_fd).strip().split(",")

        except StopIteration:
            # headerless csv or empty file
            return [], ""

        csv_commas = len(headers) - 1

        for csv_entry in csv_fd:
            csv_line_data: dict[str, str | int] = {}

            values = csv_entry.strip().split(
                ",",
                maxsplit=csv_commas,
            )

            for head, val in zip(headers, values):
                val = val.strip('"')

                if val.isdigit():
                    csv_line_data.update({head: int(val)})

                else:
                    csv_line_data.update({head: val})

            csv_data.append(csv_line_data)

    return csv_data, "".join(prelines)


def utils_input_int(
    message: str,
    message_nonint: str,
    message_bounds: str,
    left_bound: int = 0,
    right_bound: int = 100,
) -> int:
    """
    utility function to prompt user for and validate integer

    arguments
        message: str
            default message given, formatting available with keyword 'query'
        alt_message: str
            message given when previous input was a non-integer
        left_bound: int = 0
            inclusive left integer boundary for validation
        right_bound: int = 100
            inclusive left integer boundary for validation

    returns int
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    query = input(message)

    check_bounds, check_is_digit = False, False
    while not (
        (check_is_digit := query.isdigit())
        and (check_bounds := (left_bound <= int(query) <= right_bound))
    ):
        if not check_is_digit:
            query = input(message_nonint.format(query=query))
        elif not check_bounds:
            query = input(message_bounds.format(query=query))

    return int(query)


def utils_url_get(url: str) -> dict | None:
    """
    utility function to attempt to GET request a url

    arguments
        url: str
            fully-fledged valid uri to request to

    returns dict | None
        dict: request and parsing was successful
        None: unsuccessful request and parsing, fallback return value
    """
    data = {}

    try:
        # use urllib.request.urlopen to get response from api
        with urlopen(url) as response:
            # read response
            body = response.read()

            # attempt to decode response as url
            try:
                data = loads(body)

            # return None if errored
            except JSONDecodeError as err:
                print(f"Error: Unable to decode response from data.gov.sg ({err})")
                return None

            else:
                return data

    except Exception as err:
        print(f"Error: Unable to communicate with data.gov.sg ({err})")

    return None


def utils_get_realtime_carpark_avail() -> None | tuple[str, list[dict], int]:
    """
    utility function to attempt to GET current carpark availability from data.gov.sg

    returns None | tuple[str, list[dict], int]
        None: unable to retrieve or parse data
        tuple[str, list[dict], int]: timestamp, data, number of parse failures
    """
    DGS_API = "https://api.data.gov.sg/v1"
    ENDPOINT_CP_AVAIL = "/transport/carpark-availability"

    rt_cp_avail: dict | None = utils_url_get(DGS_API + ENDPOINT_CP_AVAIL)

    if rt_cp_avail is None:
        return None

    # safely get values
    rt_cp_avail_data_raw = {}
    rt_cp_avail_data: list[dict[str, str | int]] = []

    if len(rt_cp_avail.get("items", [])) > 0:
        rt_cp_avail_data_raw = rt_cp_avail["items"][0]

    timestamp: str = "Timestamp: " + rt_cp_avail_data_raw.get("timestamp", "unknown")

    failures: int = 0
    for carpark in rt_cp_avail_data_raw.get("carpark_data", []):
        try:
            rt_cp_avail_data.append(
                {
                    "Carpark Number": carpark["carpark_number"],
                    "Total Lots": int(carpark["carpark_info"][0]["total_lots"]),
                    "Lots Available": int(carpark["carpark_info"][0]["lots_available"]),
                }
            )

        except Exception:
            failures += 1
            pass

    return (timestamp, rt_cp_avail_data, failures)


# --- menu functionality functions --- #


def menu_exit(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function: exit program

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    exit()  # :o


def menu_display_cp_info_ntotal(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function: display total carparks in CARPARK_INFORMATION

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    cp_info_len = len(state.get("csv_carpark_info", []))
    print(f"Total number of carparks in '{CSV_CARPARK_INFO}': {cp_info_len}")
    return {}


def menu_display_cp_info_basement(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function:
    display carparks in CARPARK_INFORMATION with carpark type "BASEMENT CAR PARK"

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    data_cp_info: list[dict[str, str | int]] = state["csv_carpark_info"]

    # Option 2: Display All Basement Carparks in 'carpark-information.csv'
    # Carpark No Carpark Type       Address
    # 1234567890-1234567890123345678-
    output_fmt = "{cp_no:<10} {cp_type:<18} {cp_address}"

    print(
        output_fmt.format(
            cp_no="Carpark No",
            cp_type="Carpark Type",
            cp_address="Address",
        )
    )

    total = 0
    for cp in data_cp_info:
        if cp["Carpark Type"] == "BASEMENT CAR PARK":
            print(
                output_fmt.format(
                    cp_no=cp["Carpark Number"],
                    cp_type=cp["Carpark Type"],
                    cp_address=cp["Address"],
                )
            )
            total += 1

    print(f"Total number: {total}")

    return {}


def menu_read_cp_avail(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function:
    read carpark availability data from either a csv given by the user
    or from data.gov.sg

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire

    returns dict[str, Any]
        if carpark information was not previously read, return dict will be carpark
        information data, else empty
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    cp_avail: list[dict[str, str | int]] = [{}]
    response = {}  # type: dict[str, Any]

    prompt = input("Get real-time data from data.gov.sg? (Y/N) ").upper()
    while prompt not in ["Y", "N"]:
        prompt = input(
            "Invalid response. Get real-time data from data.gov.sg? (Y/N) "
        ).upper()

    if prompt == "Y":
        _cp_avail = utils_get_realtime_carpark_avail()

        if _cp_avail is None:
            # error message is printed in utils_get_realtime_carpark_avail
            return {}

        timestamp, cp_avail, failures = _cp_avail
        if failures > 0:
            print(
                f"Warning: encountered {failures} failures processing {len(cp_avail)} processed car parks."
            )

        print(timestamp)

        response = {
            "csv_carpark_avail": cp_avail,
            "csv_carpark_avail_timestamp": timestamp,
            "csv_carpark_avail_isrealtime": True,
        }

    else:
        prompt = "Enter the file name: "

        while cp_avail == [{}]:
            try:
                filename = input(prompt)
                cp_avail, timestamp = utils_csv_read(filename, startline=1)

            except FileNotFoundError:
                prompt = "Non-existent file, please enter another file name: "

            except Exception as e:
                print(f"Error: {e}")
                return response

        print(timestamp.strip())

        response = {
            "csv_carpark_avail": cp_avail,
            "csv_carpark_avail_timestamp": timestamp.strip(),
            "csv_carpark_avail_isrealtime": False,
            "csv_carpark_avail_lastupdated": datetime.now(),
        }

    return response


def menu_display_cp_avail_ntotal(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function: display total carparks in state['csv_carpark_avail']

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    cp_avail_len: int = len(state["csv_carpark_avail"])
    print(f"Total Number of Carparks in the File: {cp_avail_len}")
    return {}


def menu_display_cp_avail_full(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function:
    display carparks in state['csv_carpark_avail'] with 0 available lots

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    data_cp_avail: list[dict[str, str | int]] = state["csv_carpark_avail"]

    total = 0
    for cp in data_cp_avail:
        if cp["Lots Available"] == 0:
            print(f"Carpark Number: {cp['Carpark Number']}")
            total += 1

    print(f"Total number: {total}")

    return {}


def menu_display_cp_avail_xavail(
    state,  # type: dict[str, Any]
    show_address: bool = False,
):  # type: (...) -> dict[str, Any]
    """
    menu option function:
    displays carparks in state['csv_carpark_avail'] with x% available lots

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
        show_address: bool = False
            show address in output
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    min_percentage = utils_input_int(
        message="Enter the percentage required: ",
        message_nonint="Unknown integer value '{query}', please re-enter the percentage required: ",
        message_bounds="Percentage should be from 0-100 inclusive, please re-enter the percentage required: ",
        left_bound=0,
        right_bound=100,
    )

    # Option 6: Display Carparks With At Least x% Available Lots
    # Enter the percentage required: 95
    # Carpark No  Total Lots  Lots Available  Percentage  Address
    # 1234567890--1234567890--12345678901234--1234567890--

    output_fmt = "{cp_no:<10}  {lots_total:>10}  {lots_avail:>14}  {percentage:>10}"

    if show_address:
        output_fmt += "  {address}"

    print(
        output_fmt.format(
            cp_no="Carpark No",
            lots_total="Total Lots",
            lots_avail="Lots Available",
            percentage="Percentage",
            address="Address",
        )
    )

    data_cp_info: list[dict[str, str | int]] = state["csv_carpark_info"]
    data_cp_avail: list[dict[str, str | int]] = state["csv_carpark_avail"]

    total = 0
    for cp in data_cp_avail:
        cp_no = cp["Carpark Number"]
        lots_total = cp["Total Lots"]
        lots_avail = cp["Lots Available"]

        corresponding_cpi = [
            cpi_cp for cpi_cp in data_cp_info if (cpi_cp["Carpark Number"] == cp_no)
        ]

        cp_address: str | int = "-"
        if len(corresponding_cpi) > 0:
            cp_address = corresponding_cpi[0]["Address"]

        if int(lots_total) == 0:
            continue

        percentage = round((int(lots_avail) / int(lots_total)) * 100, 1)

        if percentage >= min_percentage:
            print(
                output_fmt.format(
                    cp_no=cp_no,
                    lots_total=lots_total,
                    lots_avail=lots_avail,
                    percentage=percentage,
                    address=cp_address,
                )
            )

            total += 1

    print(f"Total number: {total}")

    return {}


def menu_display_cp_avail_xavail_address(
    state,
):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    menu option function:
    displays carparks in state['csv_carpark_avail'] with x% available lots
    and with addresses

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    return menu_display_cp_avail_xavail(state=state, show_address=True)


def menu_adv_display_cp_location(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    (advanced requirement) menu option function: displays all carparks at given location

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    output_fmt = (
        "{cp_no:<10}  {lots_total:>10}  {lots_avail:>14}  {percentage:>10}  {address}"
    )
    location = input("Enter a location: ").upper()

    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    data_cp_info: list[dict[str, str | int]] = state["csv_carpark_info"]
    data_cp_avail: list[dict[str, str | int]] = state["csv_carpark_avail"]

    total: int = 0
    for cpi_cp in data_cp_info:
        if location in str(cpi_cp["Address"]):
            cp_no = cpi_cp["Carpark Number"]
            address = cpi_cp["Address"]

            lots_total: str | int = "-"
            lots_avail: str | int = "-"
            percentage: str = "-"

            corresponding_cpa = [
                _cpa_cp for _cpa_cp in data_cp_avail if _cpa_cp["Carpark Number"] == cp_no
            ]
            if len(corresponding_cpa) > 0:
                lots_total = corresponding_cpa[0]["Total Lots"]
                lots_avail = corresponding_cpa[0]["Lots Available"]
                if lots_total != 0:
                    percentage = str(round(int(lots_avail) / int(lots_total) * 100, 1))

            if total == 0:
                # if we are in this code block, then the algorithm has found the first
                # carpark that matches the location query, and as such we can print the
                # table header
                #
                # if this was run before this the `for cpi_cp in data_cp_info` for loop,
                # the header would've printed even if there were no matching locations.

                print(
                    output_fmt.format(
                        cp_no="Carpark No",
                        lots_total="Total Lots",
                        lots_avail="Lots Available",
                        percentage="Percentage",
                        address="Address",
                    )
                )

            print(
                output_fmt.format(
                    cp_no=cp_no,
                    lots_total=lots_total,
                    lots_avail=lots_avail,
                    percentage=percentage,
                    address=address,
                )
            )
            total += 1

    print(
        f"No carparks found matching '{location}'."
        if total == 0
        else f"Found {total} carparks matching '{location}'."
    )

    return {}


def menu_adv_display_cp_mostlots(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    (advanced requirement) menu option function:
    display carpark with the most parking lots

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    data_cp_info: list[dict[str, str | int]] = state["csv_carpark_info"]
    data_cp_avail: list[dict[str, str | int]] = state["csv_carpark_avail"]

    highest_cp_cpa: dict[str, str | int] = {"Total Lots": -1}

    for cpa_cp in data_cp_avail:
        if int(cpa_cp["Total Lots"]) > int(highest_cp_cpa["Total Lots"]):
            highest_cp_cpa = cpa_cp

    # Carpark No  Carpark Type                     Parking System Type  Address
    # 1234567890--1234567890123456789012345678901--1234567890123456789--
    #             MECHANISED AND SURFACE CAR PARK  ELECTRONIC PARKING

    output_fmt = (
        "{cp_no:<10}  {cp_type:<31}  {cp_parkingsystype:<19}  {lots_total:>10}  "
        "{lots_avail:>14}  {percentage:>10}  {address}"
    )

    print(
        output_fmt.format(
            cp_no="Carpark No",
            cp_type="Carpark Type",
            cp_parkingsystype="Parking System Type",
            lots_total="Total Lots",
            lots_avail="Lots Available",
            percentage="Percentage",
            address="Address",
        )
    )

    cp_no = highest_cp_cpa["Carpark Number"]
    lots_total = highest_cp_cpa["Total Lots"]
    lots_avail = highest_cp_cpa["Lots Available"]
    percentage = round((int(lots_avail) / int(lots_total)) * 100, 1)

    cp_type: str | int = "-"
    cp_parkingsystype: str | int = "-"
    address: str | int = "-"

    corresponding_cpi = [
        cpi_cp for cpi_cp in data_cp_info if (cpi_cp["Carpark Number"] == cp_no)
    ]
    if len(corresponding_cpi) > 0:
        cp_type = corresponding_cpi[0]["Carpark Type"]
        cp_parkingsystype = corresponding_cpi[0]["Type of Parking System"]
        address = corresponding_cpi[0]["Address"]

    print(
        output_fmt.format(
            cp_no=cp_no,
            cp_type=cp_type,
            cp_parkingsystype=cp_parkingsystype,
            lots_total=lots_total,
            lots_avail=lots_avail,
            percentage=percentage,
            address=address,
        )
    )

    return {}


def menu_adv_write_cp_avail_addresss(state):  # type: (dict[str, Any]) -> dict[str, Any]
    """
    (advanced requirement) menu option function:
    write a carpark availability csv with addresses to TARGET_FILE

    arguments:
        state: dict[str, Any]
            program state dictionary passed from mainloop_fire
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 13/08/2023

    TARGET_FILE = "carpark-availability-with-addresses.csv"
    data_cp_info: list[dict[str, str | int]] = state["csv_carpark_info"]
    data_cp_avail: list[dict[str, str | int]] = state["csv_carpark_avail"]

    # process carparks
    cp_avail_waddr_data: list[tuple[str, int, int, str]] = [()]  # type: ignore

    for cp in data_cp_avail:
        cp_no = cp["Carpark Number"]
        lots_total = cp["Total Lots"]
        lots_avail = cp["Lots Available"]

        corresponding_cpi = [
            cpi_cp for cpi_cp in data_cp_info if (cpi_cp["Carpark Number"] == cp_no)
        ]

        cp_address: str | int = ""
        if len(corresponding_cpi) > 0:
            cp_address = corresponding_cpi[0]["Address"]

        cp_avail_waddr_data.append(
            (str(cp_no), int(lots_total), int(lots_avail), str(cp_address))
        )

    # write data
    lines = 0
    with open(TARGET_FILE, "w", encoding="utf-8") as cpaa_csv_fd:
        cpaa_csv_fd.write(state["csv_carpark_avail_timestamp"] + "\n")
        cpaa_csv_fd.write(
            ",".join(["Carpark Number", "Total Lots", "Lots Available", "Address"])
        )
        lines += 2

        # sort it as we write
        for entry in sorted(cp_avail_waddr_data[1:], key=lambda l: l[2]):
            cpaa_csv_fd.write(",".join([str(val) for val in entry]) + "\n")
            lines += 1

    print(f"{lines} lines written to '{TARGET_FILE}'.")

    return {}


# --- main program loop (mainloop) functions --- #


def mainloop_display_menu(
    menu,  # type: tuple[tuple[str, Callable[[dict[str, Any]], dict[str, Any]], str], ...]
) -> None:
    """
    main program loop (mainloop) function: displays menu

    arguments
        menu: tuple[tuple[str, Callable[[], dict[str, Any]], str]]
            tuple of tuples containing a string description, callable returning a
            dictionary to update program state with, string that if not empty is used
            to check state for a variable before running
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    print("MENU\n====")

    max_index_len: int = len(str(len(menu) - 1))

    for index, entry in enumerate(menu):
        if index == 0:
            continue

        desc, _, _ = entry
        print(f"[{str(index).rjust(max_index_len)}]  {desc}")

    print(f"[{'0'.rjust(max_index_len)}]  {menu[0][0]}")


def mainloop_input(
    state,  # type: dict[str, Any]
    menu,  # type: tuple[tuple[str, Callable[[dict[str, Any]], dict[str, Any]], str], ...]
) -> int:
    """
    main program loop (mainloop) function:
    retrieves and validates user input

    arguments
        state: dict[str, Any]
            program state dictionary
        menu: tuple[tuple[str, Callable[[dict[str, Any]], dict[str, Any]]]]
            tuple of tuples containing a string description, callable returning a
            dictionary to update program state with, string that if not empty is used
            to check state for a variable before running

    returns int
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    # first ask
    selection = utils_input_int(
        message="Enter your input: ",
        message_nonint="Unknown integer value '{query}', please re-enter your input: ",
        message_bounds=f"Menu option should be from 0 to {len(menu) - 1}, please re-enter your input: ",
        left_bound=0,
        right_bound=len(menu) - 1,
    )

    # see if any state keys are required
    _, _, required_state_key = menu[selection]

    # if required state key is not empty, check for membership in state variable
    # if state dict does not have required state key, use a while loop to reprompt
    # the user for another option
    while (required_state_key != "") and (required_state_key not in state):

        print(
            "This option is not available yet as previous options have not yet been chosen."
        )

        selection = selection = utils_input_int(
            message="Enter your input: ",
            message_nonint="Unknown integer value '{query}', please re-enter your input: ",
            message_bounds=f"Menu option should be from 0 to {len(menu) - 1}, please re-enter your input: ",
            left_bound=0,
            right_bound=len(menu) - 1,
        )

        _, _, required_state_key = menu[selection]

    return selection


def mainloop_fire(
    state,  # type: dict[str, Any]
    menu,  # type: tuple[tuple[str, Callable[[dict[str, Any]], dict[str, Any]], str], ...]
    option: int,
):  # type: (...) -> dict[str, Any]
    """
    main program loop (mainloop) function:
    fires menu callable depending on user option

    arguments
        state: dict[str, Any]
            program state dictionary
        menu
            tuple of tuples containing a string description, callable returning a
            dictionary to update program state with, string that if not empty is used
            to check state for a variable before running
        option: int
            taken from mainloop_input()

    returns None
    """
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    # retrieve details of menu option
    desc, func, _ = menu[option]

    print(f"\nOption {option}: {desc}")

    # call menu option callable and store response
    result = func(state)

    # validate response
    if isinstance(result, dict):
        return result
    return {}


# --- command-line entry functions --- #


def main() -> None:
    """command-line entry function"""
    # Mark Joshwel - SXXXXXXXX (P12) - 12/08/2023

    # shared program state is done through a dict because (ahem) no imports
    state = {
        # i argue this is start of program exection,
        # because the program starts at main()
        "csv_carpark_info": utils_csv_read(CSV_CARPARK_INFO)[0],
    }  # type: dict[str, Any]

    menu = (
        (
            "Exit",
            menu_exit,
            "",
        ),
        (
            "Display Total Number of Carparks in 'carpark-information.csv'",
            menu_display_cp_info_ntotal,
            "",
        ),
        (
            "Display All Basement Carparks in 'carpark-information.csv'",
            menu_display_cp_info_basement,
            "",
        ),
        (
            "Read Carpark Availability from Data File or data.gov.sg",
            menu_read_cp_avail,
            "",
        ),
        (
            "Print Total Number of Carparks in the Data Read in [3]",
            menu_display_cp_avail_ntotal,
            "csv_carpark_avail",
        ),
        (
            "Display Carparks Without Available Lots",
            menu_display_cp_avail_full,
            "csv_carpark_avail",
        ),
        (
            "Display Carparks With At Least x% Available Lots",
            menu_display_cp_avail_xavail,
            "csv_carpark_avail",
        ),
        (
            "Display Addresses of Carparks With At Least x% Available Lots",
            menu_display_cp_avail_xavail_address,
            "csv_carpark_avail",
        ),
        (
            "Display All Carparks at Given Location",
            menu_adv_display_cp_location,
            "csv_carpark_avail",
        ),
        (
            "Display Carpark with the Most Parking Lots",
            menu_adv_display_cp_mostlots,
            "csv_carpark_avail",
        ),
        (
            "Create an Output File with Carpark Availability with Addresses and Sort by Lots Available",
            menu_adv_write_cp_avail_addresss,
            "csv_carpark_avail",
        ),
    )  # type: tuple[tuple[str, Callable[[dict[str, Any]], dict[str, Any]], str], ...]

    option: int = -1  # backup sentinel
    while option != 0:
        # show menu and retrieve user input
        mainloop_display_menu(menu)
        option = mainloop_input(state, menu)

        # run menu option callable function
        response = mainloop_fire(state, menu, option)

        # update program state using response from callable
        state.update(response)

        print()


if __name__ == "__main__":
    main()
