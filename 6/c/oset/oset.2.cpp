#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <set>

typedef struct {
    PyObject_HEAD
    /* Type-specific fields go here. */
    std::set<int> s;
} oset_t;

static void
oset_dealloc(oset_t *o)
{
    Py_TYPE(o)->tp_free((PyObject *)o);
}

static int
oset_traverse(oset_t *o, visitproc visit, void *arg)
{
    return 0;
}

static PyObject *
oset_add(oset_t *self, PyObject *args)
{
    long int num = 0;

    if (!PyArg_ParseTuple(args, "l", &num))
        return NULL;

    self->s.insert(num);
    return Py_None;
}

static PyObject *
oset_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    oset_t *self;

    self = (oset_t *)type->tp_alloc(type, 0);
    if (self == NULL) {
        return PyErr_NoMemory();
    }

    self->s = std::set<int>();
    return (PyObject *)self;
}

static int
oset_init(oset_t *self, PyObject *args, PyObject *kwds)
{
    self->s.clear();
    return 0;
}


static Py_ssize_t
oset_length(oset_t *self)
{
    return Py_ssize_t(self->s.size());
}

static int
oset_contains(oset_t *self, PyObject *arg)
{
    if (!PyLong_Check(arg)) {
        PyErr_SetString(PyExc_TypeError, "object must be number");
        return -1;
    }

    long int num = PyLong_AsLong(arg);

    if (self->s.find(num) != self->s.end()) {
        return 1;
    }
    return 0;
}


static PySequenceMethods oset_as_sequence = {
    (lenfunc)oset_length,                            /* sq_length */
    0,                                               /* sq_concat */
    0,                                               /* sq_repeat */
    0,                                               /* sq_item */
    0,                                               /* sq_slice */
    0,                                               /* sq_ass_item */
    0,                                               /* sq_ass_slice */
    (objobjproc)oset_contains,                       /* sq_contains */
};


static PyMethodDef oset_methods[] = {
    {"add",    (PyCFunction) oset_add, METH_VARARGS},
    {NULL,     NULL}           /* sentinel */
};

PyTypeObject oset_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "oset.OSet",                                     /* tp_name */
    sizeof(oset_t),                                  /* tp_basic_size */
    0,                                               /* tp_itemsize */
    (destructor)oset_dealloc,                        /* tp_dealloc */
    0,                                               /* tp_print */
    0,                                               /* tp_getattr */
    0,                                               /* tp_setattr */
    0,                                               /* tp_reserved */
    0, //(reprfunc)oset_repr,                             /* tp_repr */
    0,                                               /* tp_as_number */
    &oset_as_sequence,                               /* tp_as_sequence */
    0,                                               /* tp_as_mapping */
    0,                                               /* tp_hash */
    0,                                               /* tp_call */
    0,                                               /* tp_str */
    0,                                               /* tp_getattro */
    0,                                               /* tp_setattro */
    0,                                               /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,        /* tp_flags */
    0,                                               /* tp_doc */
    (traverseproc)oset_traverse,                     /* tp_traverse */
    0,                                               /* tp_clear */
    0,                                               /* tp_richcompare */
    0,                                               /* tp_weaklistoffset */
    0,                                               /* tp_iter */
    0,                                               /* tp_iternext */
    oset_methods,                                    /* tp_methods */
    0,                                               /* tp_members */
    0,                                               /* tp_getset */
    0,                                               /* tp_base */
    0,                                               /* tp_dict */
    0,                                               /* tp_descr_get */
    0,                                               /* tp_descr_set */
    0,                                               /* tp_dictoffset */
    (initproc)oset_init,                             /* tp_init */
    0,                                               /* tp_alloc */
    oset_new,                                        /* tp_new */
    0,                                               /* tp_free */
};

static struct PyModuleDef oset_module = {
    PyModuleDef_HEAD_INIT,
    "oset",   /* name of module */
    NULL,     /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
};


PyMODINIT_FUNC
PyInit_oset(void)
{
    PyObject *m;
    if (PyType_Ready(&oset_Type) < 0)
        return NULL;

    m = PyModule_Create(&oset_module);
    if (m == NULL)
        return NULL;

    Py_INCREF(&oset_Type);
    PyModule_AddObject(m, "OSet", (PyObject *) &oset_Type);
    return m;
}