#include <pybind11/pybind11.h>

namespace py = pybind11;

// A simple function to test C++ integration
int add(int a, int b) {
    return a + b;
}

// Expose the function to Python
PYBIND11_MODULE(pybase_cpp, m) {
    m.def("add", &add, "A function that adds two numbers");
}
