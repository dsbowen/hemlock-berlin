from hemlock import Input, Page, Submit as S

CORRECT_1 = 25
CORRECT_2A = 30
CORRECT_2B = 20
CORRECT_3 = 50

def berlin():
    return Page(
        Input(
            '''
            <p>Out of 1,000 people in a small town 500 are members of a 
            choir. Out of these 500 members in the choir 100 are men. Out 
            of the 500 inhabitants that are not in the choir 300 are men. 
            What is the probability that a randomly drawn man is a member 
            of the choir? Please indicate the probability in percent.</p>
            ''',
            append='%', input_type='number', submit=S(_verify1)
        )
    )

def _verify1(q1):
    if q1.data != CORRECT_1:
        page = Page(
            Input(
                '''
                <p>Imagine we are throwing a five-sided die 50 times. On 
                average, out of these 50 throws how many times would this 
                five-sided die show an odd number (1, 3, or 5)?</p>
                ''',
                append='out of 50 throws', input_type='number', var='Berlin',
                submit=S(_verify2a)
            )
        )
    else:
        page = Page(
            Input(
                '''
                <p> Imagine we are throwing a loaded die (6 sides). The 
                probability that the die shows a 6 is twice as high as the 
                probability of each of the other numbers. On average, out 
                of these 70 throws how many times would the die show the 
                number 6?</p>
                ''',
                append='out of 70 throws', input_type='number',
                submit=S(_verify2b)
            )
        )
    q1.branch.pages.insert(q1.page.index+1, page)

def _verify2a(q2a):
    q2a.data = 1 if q2a.data != CORRECT_2A else 2

def _verify2b(q2b):
    if q2b.data == CORRECT_2B:
        q2b.var, q2b.data = 'Berlin', 4
    else:
        page = Page(
            Input(
                '''
                <p>In a forest 20% of mushrooms are red, 50% brown, and 30% 
                white. A red mushroom is poisonous with a probability of 
                20%. A mushroom that is not red is poisonous with a 
                probability of 5%. What is the probability that a poisonous 
                mushroom in the forest is red?</p>
                ''',
                append='%', input_type='number', var='Berlin',
                submit=S(_verify3)
            )
        )
        q2b.branch.pages.insert(q2b.page.index+1, page)

def _verify3(q3):
    q3.data = 3 if q3.data != CORRECT_3 else 4