# Register your students parents in WebUntis
This tool lets you trigger the first step of registration for your students parents on WebUntis.
You can take a text file with email addresses of the parents to let the script run through that 
list and fill each email into the official registration form of WebUntis. After that the parents
will get a registration email from WebUntis to complete their registration.
This way it'S more easy for the parents to get in.

## Usage
1. Get a list of emails like this one.
```
some@one.com
you@guugle.es
...
```
2. Install requirements
`pip install -r requirements.txt`

3. Run the script with arguments
`python register_parents.py --school-url nessa.webuntis.com --mails path/to/parentsmail.txt`

