Streamlabs Loyalty Points Leaderboard 

Purpose:
This application fetches and displays the loyalty points leaderboard for a Twitch streamer's channel using the Streamlabs API.
It is currently a WIP.

Prerequisites:
- Python 3.7 or higher
- requests library

Setup:
1. Download the repository here https://github.com/ChristianRansom/LoyaltyLeaderboards/tree/master
2. Install the python requirements


Configuration:
1. Open '.env' in a text editor
2. Replace 'your_client_id_here' with the provided client ID
3. Replace 'your_client_secret_here' with the provided client secret

Running the Application:
1. Open a command prompt or terminal
2. Navigate to the directory containing the script
3. Run the script by typing: python loyalty_points_fetcher.py
4. The script will display a URL. Copy this URL and open it in a web browser
5. Log in to Streamlabs if prompted and authorize the application
6. You will be redirected to a URL starting with 'http://localhost:8000/callback'
7. Copy the 'code' parameter from this URL
8. Paste the code into the command prompt when prompted

Expected Output:
If successful, the application will display the loyalty points leaderboard data in JSON format.

Troubleshooting:
- If you encounter a 'ModuleNotFoundError', ensure you've installed the requests library
- If you get an authorization error, double-check that you've entered the correct client ID and secret
- If you receive a 401 error after authorization, it means the application is working correctly but awaiting approval for loyalty points access

For any other issues, please contact christian.ransom123@gmail.com
