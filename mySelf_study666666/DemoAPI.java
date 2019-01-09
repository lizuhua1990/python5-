





public class DemoAPI{
    @RequestMapping(value="/getDemo/{userName}",method=RequestMethod.GET)
    public String getDemo(@PathVariable String userName){
    //String i="aaaa"
    //userName=userName+i;
        return"您输入的数据是"+userName；
    }
    public static int count =0;
    @RequestMapping(value="/postDemo".method=RequestMethod.POST)
    public String postDemo(@RequestParam String userName){
        count++;
        String reslt ="接口是第"+count+"测被调用，您的用户是"+userName;
        return result;
    }
}