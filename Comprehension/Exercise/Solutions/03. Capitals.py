
country = input().split(', ')
capital = input().split(', ')

result = {country[index]: capital[index]for index in range(len(country))}

print(*[f"{key} -> {value}"for key, value in result.items()], sep='\n')