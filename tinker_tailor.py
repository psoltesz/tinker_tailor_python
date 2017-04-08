import time


class TinkerTailor:

    @staticmethod
    def run(n, k):
        start_time = time.time()
        number_list = list(range(1, n + 1))
        losers = []
        k -= 1
        idx = k
        while len(number_list) > 1:
            losers.append(number_list.pop(idx))
            idx = (idx + k) % len(number_list)
        print("Process took %s seconds." % (time.time() - start_time))
        print("Losers:", losers)
        print("Winner:", number_list[0])


if __name__ == "__main__":
    TinkerTailor.run(5, 3)
