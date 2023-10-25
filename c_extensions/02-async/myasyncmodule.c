#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "threadedcode2.h"
#include <stdio.h>

static PyObject *my_callback = NULL;

void print_result(int n)
{
  printf("[C] Yo I waited = %d seconds\n", n);

  PyObject *arglist = Py_BuildValue("(i)", n);
  PyObject *result;
  result = PyObject_CallObject(my_callback, arglist);

  Py_DECREF(arglist);
  Py_DECREF(result);
}

static PyObject *
myasync_system(PyObject *self, PyObject *args)
{
  printf("Running A C Extensions :)\n");
  PyObject *temp;

	if (PyArg_ParseTuple(args, "O:set_callback", &temp)) {
			if (!PyCallable_Check(temp)) {
					PyErr_SetString(PyExc_TypeError, "parameter must be callable");
					return NULL;
			}
			Py_XINCREF(temp);         /* Add a reference to new callback */
			Py_XDECREF(my_callback);  /* Dispose of previous callback */
			my_callback = temp;       /* Remember new callback */
			/* Boilerplate to return "None" */
			Py_INCREF(Py_None);
	}

  PyEval_InitThreads();
  call_some_threads(print_result);
  
  return PyLong_FromLong(0);
}

static PyMethodDef Methods[] = {
    {"run",  myasync_system, METH_VARARGS,
     "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "myasync",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    Methods
};

PyMODINIT_FUNC
PyInit_myasync(void)
{
    time_t t;
    srand((unsigned) time(&t));
    return PyModule_Create(&module);
}
