from modules.fancy_words_generator import get_fancy_words
from modules.phrase_translation import PhraseTranslation
from modules.question_generator import QuestionGenerator
from modules.wikipedia_search import search_wikipedia

some_words = "She had left"
text = """
 When she had left, I asked Holmes about the case. 
 'The young woman is quite interesting, but her little problem is not very difficult or unusual. Would you mind reading me the description of Hosmer Angel?' I then read it to Holmes: 
 Missing, a gentleman called Hosmer Angel. About 5ft. 7in. tall. He's strongly built with black hair, black sideboards and moustache; he's a little bald in the centre; he wears dark glasses; and he's got a speech defect. He has got a sallow complexion. He was wearing a black coat, black waistcoat, grey trousers and brown boots. Please contact Miss Sutherland etc. etc. 
 'That is enough,' said Holmes. 'Now look at these letters which Hosmer wrote to her. What do you see?' 
 'They are typed,' I said. 
 'Not only that, but the signature is typed too. The point about the signature is very suggestive - in fact, we can call it conclusive.' 
 'Of what?' 
 'My dear fellow, can't you see how important this fact is to the case?' 
 'No, I 
"""

PhraseTranslation = PhraseTranslation()
translation = PhraseTranslation.get_translation(some_words)
print(translation)

QuestionGenerator = QuestionGenerator()
questions = QuestionGenerator.generate_questions(text)
print(questions)

results = search_wikipedia("Sherlock Holmes")
print(results)

fancy_words = get_fancy_words(text)
print(fancy_words)
