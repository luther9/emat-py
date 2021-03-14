# Name

`emat` stands for "Exponential Moving Average Tracker".

# Argument

`emat` takes one argument: the name of the database to create or retrieve.
`emat` will add `.emat` to the argument to get the actual filename.

# Commands

Commands may require a track name, a date, and an amount. Arguments are
interpreted in a bash-like syntax, so you may use quotes and backslashes to make
any track name you want. If the date is omitted, `emat` will assume today's
date. No two database entries may have the same name and date. If a given
name/date combination does not yet exist, its amount is assumed to be 0.

## `set <name> <date> <amount>`

Create a database entry. If there is already an entry with the same name and
date, overwrite the amount. If there are no existing entries with the same name,
get confirmation to create a new track.

## `add <name> <date> <amount>`

Like `set`, but adds the given amount to the current amount to get the new
amount.

## `get <name> <date>`

Show the amount and moving average for the given date. If no name is given, show
a result for every name in the database.

## `list <name>`

List all entries with a non-zero amount for the given name. Include the moving
averages. If no name is given, list all entries. Results are sorted by name,
then date.

## `save`

Save the database.

To delete an entry, use `set <name> <date> 0`.

To exit the program, hit Ctrl-D.
