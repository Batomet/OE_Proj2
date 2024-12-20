import os
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class ChartsService:
    output_folder = "outputs"

    @staticmethod
    def best_chart(bests, x1, x2):
        plt.ylabel('Results')
        plt.xlabel('Epochs')
        epochs_amount = len(bests) - 1
        epochs_counter = [i + 1 for i in range(epochs_amount + 1)]
        plt.plot(epochs_counter, bests, 'r')

        plt.title('Best Result Over Epochs')
        plt.savefig(os.path.join(ChartsService.output_folder, 'best_result_chart.png'))
        plt.close()

        with open(os.path.join(ChartsService.output_folder, "results.txt"), "w") as file:
            for i in range(epochs_amount):
                file.write(f"Epoch:{epochs_counter[i]}, x1:{x1[i]}, x2:{x2[i]}, best:{bests[i]}\n")

    @staticmethod
    def average_chart(averages):
        plt.ylabel('Average result')
        plt.xlabel('Epochs')
        epochs_amount = len(averages) - 1
        epochs_counter = [i + 1 for i in range(epochs_amount + 1)]
        plt.plot(epochs_counter, averages, 'g')

        plt.title('Average Result Over Epochs')

        plt.savefig(os.path.join(ChartsService.output_folder, 'average_result_chart.png'))
        plt.close()

    @staticmethod
    def std_chart(stds):
        plt.ylabel('Std')
        plt.xlabel('Epochs')
        epochs_amount = len(stds) - 1
        epochs_counter = [i + 1 for i in range(epochs_amount + 1)]
        plt.plot(epochs_counter, stds, 'b')

        plt.title('Standard Deviation Over Epochs')

        plt.savefig(os.path.join(ChartsService.output_folder, 'std_chart.png'))
        plt.close()
