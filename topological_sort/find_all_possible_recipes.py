from typing import List, Dict


def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]: # Accepted on Leetcode
    cache = {}
    info: Dict[str, List[str]] = {}
    for index, recipe in enumerate(recipes):
        info[recipe] = ingredients[index]

    def _is_recipe_possible(my_recipe, visited):
        if my_recipe in cache:
            return cache[my_recipe]

        if my_recipe in visited:
            return False
        visited.add(my_recipe)

        is_recipe_possible = True
        for ingredient in info[my_recipe]:
            if ingredient in supplies:
                continue
            if ingredient not in recipes or not _is_recipe_possible(ingredient, visited):
                is_recipe_possible = False
                break

        cache[my_recipe] = is_recipe_possible
        return is_recipe_possible

    possible_recipes = []
    for recipe in recipes:
        if _is_recipe_possible(recipe, visited=set()):
            possible_recipes.append(recipe)

    return possible_recipes


if __name__ == "__main__":
    print(findAllRecipes(["bread", "sandwich", "burger"],
                         [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                         ["yeast", "flour", "meat"]))
