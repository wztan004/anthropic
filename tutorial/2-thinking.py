import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[{
        "role": "user",
        "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"
    }]
)
print(response.content)

# [
#     ThinkingBlock(
#         signature='x', 
#         thinking="This is a classic question in number theory. The user is asking whether there are infinitely many prime numbers that are congruent to 3 modulo 4.\n\nLet me think about this systematically.\n\nFirst, let me recall what primes congruent to 3 mod 4 look like:\n- 3 ≡ 3 (mod 4)\n- 7 ≡ 3 (mod 4)\n- 11 ≡ 3 (mod 4)\n- 19 ≡ 3 (mod 4)\n- 23 ≡ 3 (mod 4)\n- etc.\n\nSo we want to know if there are infinitely many primes of the form 4k + 3.\n\nThis is actually a famous theorem that can be proved using a technique similar to Euclid's proof of the infinitude of primes, but with a clever twist.\n\nLet me construct the proof:\n\nSuppose there are only finitely many primes congruent to 3 modulo 4. Let's call them p₁, p₂, ..., pₙ where each pᵢ ≡ 3 (mod 4).\n\nNow consider the number N = 4(p₁p₂...pₙ) - 1.\n\nNote that N ≡ 4·(something) - 1 ≡ -1 ≡ 3 (mod 4).\n\nSince N > 1, it has at least one prime divisor. Let q be a prime divisor of N.\n\nNow, q cannot be 2, because N is odd (since N ≡ 3 (mod 4)).\n\nAlso, q cannot be any of p₁, p₂, ..., pₙ, because if q = pᵢ for some i, then pᵢ would divide both N and 4(p₁p₂...pₙ), which means pᵢ would divide their difference: 4(p₁p₂...pₙ) - N = 4(p₁p₂...pₙ) - (4(p₁p₂...pₙ) - 1) = 1. \n\nThis contradiction implies that our initial assumption must be false. There must be infinitely many primes congruent to 3 modulo 4.\n\nThe proof elegantly demonstrates that no matter how many such primes we list, we can always construct a new prime of the same form, ensuring their infinite existence.\n\nBy carefully examining the number N and its prime divisors, we reveal a fundamental property about the distribution of primes in different modular classes.\n\nI construct N with a specific form that forces a contradiction. By showing N must have a prime divisor ≡ 3 (mod 4) not among the original primes, we demonstrate an infinite sequence of such primes exists.\n\nThe key insight emerges from the modular arithmetic constraints, revealing an endless supply of primes with this specific congruence characteristic.", 
#         type='thinking'), 
#     TextBlock(citations=None, 
#               text="Yes, there are infinitely many prime numbers such that n ≡ 3 (mod 4).\n\nThis is a classic theorem in number theory that can be proven using a technique similar to Euclid's proof of the infinitude of primes. Here's the proof:\n\n**Proof by contradiction:**\n\nSuppose there are only finitely many primes congruent to 3 modulo 4. Let's call them p₁, p₂, ..., pₖ.\n\nConsider the number N = 4(p₁p₂...pₖ) - 1.\n\nNote that N ≡ 4·(something) - 1 ≡ -1 ≡ 3 (mod 4).\n\nSince N > 1, it must have at least one prime divisor. Let q be any prime divisor of N.\n\n**Key observations:**\n1. q cannot equal 2, since N is odd\n2. q cannot equal any of p₁, p₂, ..., pₖ, because if q = pᵢ, then pᵢ would divide both N and 4(p₁p₂...pₖ), implying pᵢ divides their difference: 1. This is impossible.\n3. Since q is an odd prime, either q ≡ 1 (mod 4) or q ≡ 3 (mod 4)\n\n**The crucial step:**\nIf all prime divisors of N were congruent to 1 (mod 4), then N itself would be congruent to 1 (mod 4), since the product of numbers ≡ 1 (mod 4) is also ≡ 1 (mod 4).\n\nBut we established that N ≡ 3 (mod 4), so N must have at least one prime divisor q where q ≡ 3 (mod 4).\n\nSince q is different from all the primes p₁, p₂, ..., pₖ, we've found a new prime congruent to 3 modulo 4, contradicting our assumption.\n\nTherefore, there are infinitely many primes of the form 4k + 3.\n\nSome examples: 3, 7, 11, 19, 23, 31, 43, 47, ...", 
#               type='text')
#               ]