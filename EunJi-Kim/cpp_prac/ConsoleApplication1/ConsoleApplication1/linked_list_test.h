#pragma once

#include <iostream>
#include <algorithm>

class linked_list_test {
public:
	static const int MX = 1000005;
	int dat[MX], pre[MX], nxt[MX];
	int unused = 1;

	void insert(int addr, int num)
	{
		dat[unused] = num;
		pre[unused] = addr;
		nxt[unused] = nxt[addr];
		if (nxt[addr] != -1) pre[nxt[addr]] = unused;
		nxt[addr] = unused;
		unused++;
	}

	void erase(int addr)
	{
		nxt[pre[addr]] = nxt[addr];
		if (nxt[addr] != -1) pre[nxt[addr]] = pre[addr];
	}

	void traverse()
	{
		int cur = nxt[0];
		while (cur != -1) {
			std::cout << dat[cur] << ' ';
			cur = nxt[cur];
		}
		std::cout << "\n\n";
	}

	void insert_test() {
		std::cout << "****** insert_test *****\n";
		insert(0, 10); // 10(address=1)
		traverse();
		insert(0, 30); // 30(address=2) 10
		traverse();
		insert(2, 40); // 30 40(address=3) 10
		traverse();
		insert(1, 20); // 30 40 10 20(address=4)
		traverse();
		insert(4, 70); // 30 40 10 20 70(address=5)
		traverse();
	}



	void erase_test() {
		std::cout << "****** erase_test *****\n";
		erase(1); // 30 40 20 70
		traverse();
		erase(2); // 40 20 70
		traverse();
		erase(4); // 40 70
		traverse();
		erase(5); // 40
		traverse();
	}

	void play() {
		std::fill(pre, pre + MX, -1);
		std::fill(nxt, nxt + MX, -1);
		insert_test();
		erase_test();
	}
};