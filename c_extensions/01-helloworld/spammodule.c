#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

static PyObject *my_callback = NULL;

static PyObject *
my_set_callback(PyObject *dummy, PyObject *args)
{
    PyObject *result = NULL;
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
        result = Py_None;
    }
    return result;
}

static PyObject *
spam_random(PyObject *self, PyObject *args)
{
  int value = rand();
  return PyLong_FromLong(value);
}

static PyObject *
spam_list_random(PyObject *self, PyObject *args)
{
  unsigned int count = 0;
  if (!PyArg_ParseTuple(args, "I", &count))
    return NULL;

  PyObject *outputList = PyList_New(0);
  if (!outputList)
    return NULL;

  for (unsigned int i=0; i < count; i++) {
    PyList_Append(outputList, PyLong_FromLong(rand()));
  }

  return outputList;
}


static PyObject *
spam_larger_than(PyObject *self, PyObject *args)
{
  PyObject *inputList = NULL;
  long threshold = 0;
  if (!PyArg_ParseTuple(args, "lO", &threshold, &inputList))
    return NULL;

  if (!PyList_Check(inputList))
    return NULL;

  Py_INCREF(inputList);

  Py_ssize_t inputSize = PyList_Size(inputList);

  PyObject *outputList = PyList_New(0);
  if (!outputList) {
    Py_DECREF(inputList);
    return NULL;
  }
  
  for (Py_ssize_t i=0; i < inputSize; i++) {
    PyObject *val = PyList_GetItem(inputList, i);
    if (PyLong_Check(val)) {
      long lval = PyLong_AsLong(val);
      if (lval > threshold) {
        PyList_Append(outputList, val);
      }
    }
  }

  Py_DECREF(inputList);

  return outputList;
}

static PyObject *
spam_reverse(PyObject *self, PyObject *args)
{
  const char *str;
  if (!PyArg_ParseTuple(args, "s", &str))
    return NULL;

  size_t textsize = strlen(str);
  char *result = (char *)malloc(sizeof(char) * (textsize + 1));
  if (!result) {
    return PyErr_NoMemory();
  }

  Py_BEGIN_ALLOW_THREADS
  for (size_t i=0; i < textsize; i++) {
    result[i] = str[textsize - 1 - i];
  }
  result[textsize] = '\0';
  Py_END_ALLOW_THREADS

  PyObject *res = PyUnicode_FromStringAndSize(result, textsize);
  free(result);
  return res;
}


static PyObject *
spam_fib(PyObject *self, PyObject *args)
{
  int n;
  if (!PyArg_ParseTuple(args, "i", &n))
    return NULL;

  unsigned long x = 0, y = 1;
  unsigned long temp;

  for (int i=0; i < n; i++) {
    temp = x;
    x = y;
    y = temp + x;
  }

  return PyLong_FromUnsignedLong(y);
}


static PyObject *
spam_system(PyObject *self, PyObject *args)
{
  const char *command;
  int sts;

  printf("Running A C Extensions :)\n");

  if (!PyArg_ParseTuple(args, "s", &command))
    return NULL;
  sts = system(command);
  return PyLong_FromLong(sts);
}

static PyMethodDef SpamMethods[] = {
    {"system",  spam_system, METH_VARARGS,
     "Execute a shell command."},
    {"fib", spam_fib, METH_VARARGS,
      "calculate n fibonacci number"},
    {"rev", spam_reverse, METH_VARARGS,
      "reverses a string"},
    {"larger_than", spam_larger_than, METH_VARARGS,
      "returns numbers larger than threshold"},
    {"rand", spam_random, METH_VARARGS,
      "returns a random int"},
    {"randlist", spam_list_random, METH_VARARGS,
      "returns a list of random numbers"},

    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
    PyModuleDef_HEAD_INIT,
    "spam",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    time_t t;
    srand((unsigned) time(&t));
    return PyModule_Create(&spammodule);
}
