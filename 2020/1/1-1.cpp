#include <algorithm>
#include <cstdio>
#include <iostream>
int main()
{
  freopen("in.txt", "r", stdin);
  int count = 0;
  int num[202];
  while (scanf("%d\n", &num[count]) == 1)
  {
    count++;
  }
  fclose(stdin);
  std::sort(num, num + count);
  /*for (int i = 0; i < count; ++i)
  {
    std::cout << num[i] << std::endl;
  }*/

  bool found = false;
  for (int i = 0; i < count; ++i)
  {
    for (int j = i + 1; j < count;)
    {
        auto sum = num[i] + num[j];
        if (sum < 2020)
        {
          j++;
        }
        else if (sum == 2020)
        {
          found = true;
          std::cout << "Found " << num[i] << ", " << num[j] << std::endl;
          std::cout << "sum: " << num[i] * num[j] << std::endl;
          break;
        }
        else
        {
          break;
        }
    }

    if (found) break;
  }
  return 0;
}
