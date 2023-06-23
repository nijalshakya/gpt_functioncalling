import requests

print(
    requests.post(
        "http://localhost:10000",
        json={
            "from_email": "zubra@gmail.com",
            "content": """
                dear nijal
                i am milli form guccci. we are a team of 10000 people, i want 2 t shirt & 1 pant for each member, and i will get 5 pairs of shoes;

                can you let me know the price of best product you have and how soon can it be delivered?

                thanks
                
                milli,gucci
                """
        }
    ).json()
    
)
