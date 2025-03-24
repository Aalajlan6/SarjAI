import requests
import os
import openai
import networkx as nx
import matplotlib.pyplot as plt



def get_content(book_id):

    content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    metadata_url = f"https://www.gutenberg.org/ebooks/{book_id}"

    # Get book content
    content_response = requests.get(content_url)
    content = content_response.text

    #print(content[0:len(content)//100])

    # Get metadata
    metadata_response = requests.get(metadata_url)
    return content, metadata_response.text




def generate_list_of_interactions(content):
    client = openai.OpenAI(
        api_key="37e22f43-0bd5-4862-974e-bbc1340fb984",
        base_url="https://api.sambanova.ai/v1",
    )

    response = client.chat.completions.create(
        model="Llama-3.1-Swallow-70B-Instruct-v0.3",

        messages = [
        {"role": "system", "content": "Provide only the final answer. Do not include any internal chain-of-thought or explanations. i.e (Here are the character interactions from the)"},
        {
            "role": "user",
            "content": (
                "Please provide every character interaction as a list of tuples like (charA, charB). Stick to this format and this format only. Do not do anything diffierent from the format"
                "don't use bullet point or any other formatting (don'nt write * before each one)."
                "using just first names for the first chapter. Filter out duplicates. "
                "Please only provide the list. "
                + content[0:len(content)//10] +
                "please only use this format and no other format. here is an exacty template I want you to follow:"
                "(charA, charB)"
                "(charC, charD)"
                "(charA, charC)"
                "(charB, charD)"
            )
        }
        ],
        temperature=0.1,
        top_p=0.1,
    )
    print(response.choices[0].message.content)
    interaction_list = response.choices[0].message.content.split("\n")
    return interaction_list



def generate_graph(list):
    g = nx.Graph()
    for interaction in list:
        interaction = interaction[1:-1]
        interaction = interaction.split(", ")
        g.add_edge(interaction[0], interaction[1])
    nx.draw(g, with_labels=True)
    plt.show()

def main():
    # book_id = 123
    # content, metadata = get_content(book_id)
    # interactions = generate_list_of_interactions(content)
    # print(interactions)
    # #example ["('Bob', 'Beulah')", "('Jim', 'Bob')", "('Bob', 'Beulah')"]
    temp = [
    "(Arthur, Gwen)",
    "(Gwen, Arthur)",
    "(Arthur, Lancelot)",
    "(Lancelot, Arthur)",
    "(Morgan, Gwen)",
    "(Gwen, Morgan)",
    "(Morgan, Lancelot)",
    "(Lancelot, Morgan)",
    "(Mordred, Arthur)",
    "(Arthur, Mordred)",
    "(Mordred, Morgan)",
    "(Morgan, Mordred)",
    "(Percival, Gwen)",
    "(Gwen, Percival)",
    "(Percival, Lancelot)",
    "(Lancelot, Percival)"
    ]
    generate_graph(temp)
main()