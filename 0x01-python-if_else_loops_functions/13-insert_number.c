#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - add node to sorted list
 * @number: new node data
 * @head: head to nodes
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *h;

	ptr = malloc(sizeof(listint_t));

	if (ptr == NULL)
		return (NULL);
	ptr->n = number;
	ptr->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		*head = ptr;
		return (ptr);
	}
	h = *head;
	while (h->next != NULL && h->next->n < number)
		h = h->next;

	ptr->next = h->next;
	h->next = ptr;

	return (ptr);
}
