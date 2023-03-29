import os
import openai



openai.api_key = ""

def generate_book_outline(prompt, max_tokens=1000, n=1):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_chapter_content(prompt, max_tokens=3048, n=1):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    # Get user input for book topic
    book_topic = input("Enter a book topic: ")

    # Generate book outline
    outline_prompt = f"Create a book outline with chapters and sections for a book about {book_topic}:"
    book_outline = generate_book_outline(outline_prompt)
    print("Book Outline:")
    print(book_outline)

    # Generate content for each chapter
    chapters = book_outline.split("\n")
    book_content = []
    for chapter in chapters:
        content_prompt = f"Write a detailed chapter for a book about {chapter}:"
        chapter_content = generate_chapter_content(content_prompt)
        book_content.append(chapter_content)

    # Save the generated book to a file
    with open("generated_book.txt", "w") as file:
        for chapter, content in zip(chapters, book_content):
            file.write(chapter + "\n")
            file.write(content + "\n\n")

    print("The generated book has been saved to 'generated_book.txt'")

if __name__ == "__main__":
    main()



