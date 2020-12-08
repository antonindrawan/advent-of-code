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
    for (int j = i + 1; j < count; ++j)
    {
      for (int k = j + 1; k < count;)
      {
        auto sum = num[i] + num[j] + num[k];
        if (sum < 2020)
        {
          k++;
        }
        else if (sum == 2020)
        {
          found = true;
          std::cout << "Found " << num[i] << ", " << num[j] << ", " << num[k] << std::endl;
          std::cout << "sum: " << num[i] * num[j] * num[k] << std::endl;
          break;
        }
        else
        {
          break;
        }
      } 
    }

    if (found) break;
  }
  return 0;
}
