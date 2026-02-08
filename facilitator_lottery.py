import random

class FacilitatorLottery:
    def __init__(self, facilitators):
        self.facilitators = facilitators
        self.selected = None

    def draw(self):
        if not self.facilitators:
            raise ValueError("No facilitators available for draw.")
        self.selected = random.choice(self.facilitators)
        return self.selected

    def get_selected(self):
        return self.selected

# Example usage:
if __name__ == '__main__':
    facilitators = ['Alice', 'Bob', 'Charlie', 'David']
    lottery = FacilitatorLottery(facilitators)
    winner = lottery.draw()
    print(f'The selected facilitator is: {winner}')