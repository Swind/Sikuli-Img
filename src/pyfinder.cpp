#include "find-result.h"
#include "finder.h"

#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(pysikuli_img)
{
    class_<FindResult>("FindResult")
        .def(init<int, int, int, int, double>())
        .def_readwrite("x", &FindResult::x)
        .def_readwrite("y", &FindResult::y)
        .def_readwrite("w", &FindResult::w)
        .def_readwrite("h", &FindResult::h)
        .def_readwrite("score", &FindResult::score)
        .def_readwrite("text", &FindResult::text)
    ;

    void (Finder::*find_by_path)(const char*, double) = &Finder::find;
    void (Finder::*find_all_by_path)(const char*, double) = &Finder::find_all;

    class_<Finder>("Finder", init<const char*>())
      .def(init<const std::string&, int>())
      .def("setROI", &Finder::setROI)
      .def("find", find_by_path)
      .def("find", find_all_by_path)
      .def("has_next", &Finder::hasNext)
      .def("next", &Finder::next)
    ;

}

