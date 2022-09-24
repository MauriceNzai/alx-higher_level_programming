#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse - Reverses the second half of the list
 * @h2: Pointer to the head of the second half
 * Return: Nothing
 */

void reverse(listint_t **h2)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *nxt;

	prev = NULL;
	curr = *h2;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}
	*h2 = prev;
}

/**
 * compare - compares each integer of the list
 * @h1: head of the first half
 * @h2: Head of the second half
 * Return: 1 if they are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *temp1;
	listint_t *temp2;

	temp1 = h1;
	temp2 = h2;
	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - Checks ia a singly linked lis is a palindrome
 * @head: Pointer to the head of the list
 * Return: 0 if it is not a palindrone, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *nd2_half, *middle;
	int is_pal;

	slow = fast = prev_slow = *head;
	middle = NULL;
	is_pal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		nd2_half = slow;
		prev_slow->next = NULL;
		reverse(&nd2_half);
		is_pal = compare(*head, nd2_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middle->next = nd2_half;
		}
		else
		{
			prev_slow->next = nd2_half;
		}
	}
	return (is_pal);
}
