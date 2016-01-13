from temboo.Library.Google.Spreadsheets import AppendRow
from temboo.core.session import TembooSession
from data import usageLog
import credentials

# Create a session with your Temboo account details
session = TembooSession(credentials.tembooUser, credentials.tembooAppName, credentials.tembooKey)



def send_tempLog(timestamp,temp):
    # Instantiate the Choreo
    appendRowChoreo = AppendRow(session)
    # Get an InputSet object for the Choreo
    appendRowInputs = appendRowChoreo.new_input_set()

    # Set the Choreo inputs
    appendRowInputs.set_RowData(str(timestamp) + "," + str(temp))
    appendRowInputs.set_SpreadsheetTitle("TempLog")
    appendRowInputs.set_RefreshToken(credentials.googleAppRefreshToken)
    appendRowInputs.set_ClientSecret(credentials.googleAppClientSecret)
    appendRowInputs.set_ClientID(credentials.googleAppClientID)

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
    appendRowInputs.set_RefreshToken(credentials.googleAppRefreshToken)
    appendRowInputs.set_ClientSecret(credentials.googleAppClientSecret)
    appendRowInputs.set_ClientID(credentials.googleAppClientID)


    # Execute the Choreo
    appendRowResults = appendRowChoreo.execute_with_results(appendRowInputs)

    # Print the Choreo outputs
    print("Response: " + appendRowResults.get_Response())
    print("NewAccessToken: " + appendRowResults.get_NewAccessToken())
