#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info - function that prints python list
* @p: python list to print
**/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i;
	PyObject *unit, *sub;
	PyListObject *temp = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", temp->allocated);
	for (i = 0; i < size; i++)
	{
		unit = PyList_GetItem(p, i);
		sub = PyObject_Repr(unit);
		printf("Element %ld : %s\n", i, PyUnicode_AsUTF8(sub));
		Py_DECREF(sub);
	}
}
