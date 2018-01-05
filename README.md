# Cart Prices

## About
This application takes in two JSON files: a cart file and a base prices file.
It then calculates the total cart price using the information from both files in the following manner:

item price = (base_price + round(base_price * artist_markup in cents)) * quantity, where artist_markup is a percentage

The total cart price is in cents.


## To run the application:

- Clone the directory
- Use this format to run the application: `run cart.py cart-9500.json prices-ex-1.json`


### Note:
The Github user @hmc-f17-ostrich is actually a school account of mine but to avoid confusion I have changed that account username to @celine-park. I worked on this project alone.
