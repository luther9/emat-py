# Name

`emat` stands for "Exponential Moving Average Tracker".

# Usage: emat DB [FACTOR]

DB is the name of the database to create or retrieve. `emat` will add `.emat` to
the argument to get the actual filename. FACTOR is a number between 0 and 1
indicating the weight that an amount has on the average for that day. The
previous day's average has a weight of 1 - FACTOR. The default FACTOR is 0.1.

# Commands

Commands may require a track name, a date, and an amount. Arguments are
interpreted in a bash-like syntax, so you may use quotes and backslashes to make
any track name you want except the empty string. If the date is omitted, `emat`
will assume today's date. No two database entries may have the same name and
date. If a given name/date combination does not yet exist, its amount is assumed
to be 0.

## `set <name> [<date>] <amount>`

Create a database entry. If there is already an entry with the same name and
date, overwrite the amount. If there are no existing entries with the same name,
get confirmation to create a new track.

## `add <name> [<date>] <amount>`

Like `set`, but adds the given amount to the current amount to get the new
amount.

## `get [<name> [<date>]]`

Show the amount and moving average for the given date. If the name is the empty
string (the default), show a result for every name in the database.

## `list [<name>]`

List all entries with a non-zero amount for the given name. Include the moving
averages. If no name is given, list all entries. Results are sorted by name,
then date.

## `save`

Save the database.

## `factor [<dayfactor>]`

Change the day factor as described in Usage.

# Other stuff

To delete an entry, use `set <name> <date> 0`.

To exit the program, hit Ctrl-D.
