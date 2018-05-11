function set_lable(lable){
 var kernel=IPython.notebook.kernel;
 kernel.execute("lables.append("+lable+")")
 load_next_tweet();
}
function load_next_tweet(){
    var code_input="get_next_tweet()";
    var kernel=IPython.notebook.kernel;
    var callbacks={'iopub':{'output':handle_output}};
    kernel.execute(code_input,callbacks,{silent:false})
}