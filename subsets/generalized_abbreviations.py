
def generate_generalized_abbreviation(word):
    result = {str(len(word)), word}
    if len(word) == 1:
        return result

    for i in range(1, len(word)):
        for temp in generate_generalized_abbreviation(word[i:]):
            result.add(word[:i] + temp)
            if not temp[0].isdigit():
                result.add(str(len(word[:i])) + temp)

    return sorted(result)




if __name__ == "__main__":
    answer = generate_generalized_abbreviation("code")
    print(answer, len(answer))