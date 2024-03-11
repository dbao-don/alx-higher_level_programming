#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a function to check a cycle in a linked list
 * @list: pointer to a linked list to iterate.
 *
 * Return: 0 if no cycle present or 1 if cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *iterator = list;
	listint_t *jumper = list;

	while(iterator != NULL && jumper != NULL && jumper->next != NULL)
	{
		iterator = iterator->next;
		jumper = jumper->next->next;

		if (iterator == jumper)
			return (1);
	}

	return (0);
}
