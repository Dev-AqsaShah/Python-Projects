from fastapi import FastAPI
import random

app = FastAPI()

# Side hustles list
side_hustles = [
    "Freelancing - Start offering your skills online",
    "Dropshipping - Sell without handling inventory",
    "Stock Market - Invest and watch your money grow",
    "Affiliate Marketing - Earn by promoting products and services",
    "Crypto Trading - Buy and sell digital assets",
    "Online Courses - Share your knowledge and earn",
    "Print-on-Demand - Sell custom-designed products",
    "Blogging - Create content and earn through ads and sponsorships",
    "YouTube Channel - Monetize videos through ads and sponsorships",
    "Social Media Management - Manage accounts for brands and influencers",
    "App Development - Create mobile or web applications for businesses",
]

# Money quotes list
money_quotes = [
    "Money often costs too much. - Ralph Waldo Emerson",
    "A penny saved is a penny earned. - Benjamin Franklin",
    "Make money your god, and it will plague you like the devil. - Henry Fielding",
    "Too many people spend money they haven't earned to buy things they don't want. - Will Rogers",
    "Rather than love, than money, than fame, give me truth. - Henry David Thoreau"
]

@app.get("/side_hustles")
def get_side_hustles(apiKey: str):
    """Returns a random side hustle"""
    if apiKey != "1234567890":
        return {"error": "Invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    """Returns a random money quote"""
    if apiKey != "1234567890":
        return {"error": "Invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
