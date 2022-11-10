#include "ros/ros.h"
#include "testlib.h"

int main (int argc, char * argv[])
{
    ros::init(argc,argv,"test");
    testlib::Test_class class_example;
    class_example.talk();
    return 0;
}