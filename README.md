# TomTicket_Reports
A TelegramBot module for TomTicket reports

## Instalation
First you will need to download or clone this repository and put it on the modules folder.
Then edit the following files:

keys.json
```json
{
    "tt_key": "YOURTOMTICKETAPIKEY",
    "data": {
        "some_department": {
            "dp_id": "DepartmentIdHere",
            "dp_name": "DepartamentNameHere"
        },
        "another_department": {
            "dp_id": "DepartmentIdHere",
            "dp_name": "DepartamentNameHere"
        }
    }
}
```

model.txt
```text
That's some example text
 - You can put some {keywords} on it - 
 \ if you want it to have dinamic data from the API /
 
 Eg.
    The current time is {time}
    
 It will be displayed as:
    The current time is 03:46 (or whatever time it is when you give the command)
```

list.txt
```text
Put in this file just one line, it will be displayed as many times as you have open tickets in your department, and it also has keywords :)
```
## KeyWords List
KeyWords for model.txt
```python
{dp_name} = Returns the value of the dp_name of the durrent department in the keys.json
{day} = Returns the current day of the month
{month_name} = Returns the month name
{time} = Returns the current time in the format HH:MM
{waiting} = Returns the list of the wainting tickets
{in_progress} = Returns the list of the in progress tickets
{sla_out} = Returns the amount of expired tickets
{total_tickets} = Returns the total of opened tickets
```
KeyWords for list.txt
```python
{sla} = Returns an emoji according to the ticket's current SLA 
{ticket_protocol} = Returns the ticket's protocol
{ticket_title} = Returns the ticket's title
{ticket_user} = Returns the tickets's attendant
```

## Usage
Send a message in the chat as in the following example:
```
/tt dp_name
```
Where the `dp_name` is equals to one of the values you put on the keys.json attribute.

And you're done! The bot will reply with all the data you wanted.
