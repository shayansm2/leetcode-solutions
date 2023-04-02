class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions = sorted(potions, reverse=True)
        spell_indices = [i for i, _ in sorted(enumerate(spells), key=lambda x: x[1], reverse=True)]
        spells = [spells[index] for index in spell_indices]

        pairs = dict()

        last_potion_index = len(potions) - 1
        for index, spell in enumerate(spells):
            # print('spell', spell)
            while last_potion_index >= 0 and potions[last_potion_index] * spell < success:
                last_potion_index -= 1
            # print('last_potion_index', last_potion_index)
            pairs[spell_indices[index]] = last_potion_index + 1

        pairs = dict(sorted(pairs.items()))
        return pairs.values()
