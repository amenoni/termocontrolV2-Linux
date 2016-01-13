from temboo.Library.Google.Spreadsheets import AppendRow
from temboo.core.session import TembooSession
from data import usageLog

# Create a session with your Temboo account details
session = TembooSession("amenoni", "myFirstApp", "K8wciklnjD6zUZ54fdLLQRkkYBzqx1lm")



def send_tempLog(timestamp,temp):
    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)
    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
    appendRowInputs.set_RowData(str(timestamp) + "," + str(temp))
    appendRowInputs.set_SpreadsheetTitle("TempLog")
    appendRowInputs.set_RefreshToken("1/Y2R1hcipKoRzzV2r5p8Y-X1YIxDSkFoBXIyHqnMLzP0")
    appendRowInputs.set_ClientSecret("heuDjDIkCkjOak1XiZI8prat")
    appendRowInputs.set_ClientID("579401794380-3i17seip6c2b544q92ngnjcbk3ccidsd.apps.googleusercontent.com")

    # Execute the Choreo
    appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)

    # Print the Choreo outputs
    print("Response: " + appendRowResults.get_Response())
    print("NewAccessToken: " + appendRowResults.get_NewAccessToken())


def send_usageLog(usage):
    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)
    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
    appendRowInputs.set_RowData(str(usage.timestamp_UTC) + "," + str(usage.hour) + "," + str(usage.weekday) + "," + str(usage.type))
    appendRowInputs.set_SpreadsheetTitle("UsageLog")
    appendRowInputs.set_RefreshToken("1/Y2R1hcipKoRzzV2r5p8Y-X1YIxDSkFoBXIyHqnMLzP0")
    appendRowInputs.set_ClientSecret("heuDjDIkCkjOak1XiZI8prat")
    appendRowInputs.set_ClientID("579401794380-3i17seip6c2b544q92ngnjcbk3ccidsd.apps.googleusercontent.com")

    # Execute the Choreo
    appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)

    # Print the Choreo outputs
    print("Response: " + appendRowResults.get_Response())
    print("NewAccessToken: " + appendRowResults.get_NewAccessToken())
