#include "array_test.h"
#include "linked_list_test.h"

int main(void) {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);

	array_test array1;
	array1.play();

	linked_list_test* linkedList_test = new linked_list_test();
	linkedList_test->play();
	delete linkedList_test;

	return 0;
}
