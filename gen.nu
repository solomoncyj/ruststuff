def main [args: string, isdep: bool = false] {
    ansi green
    print $"processing ($args)"
    ansi reset
    # create spec file and save it
    rust2rpm $args -s --ignore-missing-license-files | save -f /dev/null
    mut crate = ""
    mut dir = ""
    mut deps: list<string> = []
    if (not $isdep) {
        #extract saved file
    $crate = (ls ($"./($args)-*.crate" | into glob)).name |get 0  
    7za x -aoa $crate | save -f /dev/null
    7za x -aoa $crate | save -f /dev/null
    $dir = ((ls ($"./($args)-*" | into glob) | where type == dir)).name |get 0 
    cd $dir
    # get licese data
    # get dependencies if not a dep
    
    $deps = (cargo-deps-list --edges normal)
        | split row "\n"
        | drop
        | str replace --regex -r 'v.*' ''
        | str trim
    cd ..
    #clean up
    rm $crate $dir --recursive
    }
    # recursively crete specs for deps
    if (not $isdep) {
        $deps| each {|in
             | main $in true}
    }
}
