def daily_temperatures(temperatures):
    stack = []
    answer = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev

        stack.append(i)

    return answer


temperatures = [73,74,75,71,69,72,76,73]

print(daily_temperatures(temperatures))