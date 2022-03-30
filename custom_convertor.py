import os

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

def run_dir(base_dir, out_dir):
    pending_list = absoluteFilePaths(base_dir)
    print(pending_list)
    count = 0;
    for iter in pending_list:
        if(iter[-4:]=='.nii'):
            #print(iter+" found!")
            os.system('/mnt/e/Code/Projects/med2image/bin/med2image -i '+iter+'    \
            -d '+out_dir+"/"+str(count)+'/   \
            -o '+str(count)+' \
            --outputFileType jpg  \
            --startSliceToConvert 140 \
            --endSliceToConvert 180')
            count = count + 1;
        else:
            pending_list.append(absoluteFilePaths(iter))

    print(str(count)+" *.nii files converted")

#run_dir('/mnt/e/ShareFolder/Datasets/PPMI_TI_3D_ControlOnly', '/mnt/e/ShareFolder/Datasets/ControlOnly_JPG')
run_dir('/mnt/e/ShareFolder/Datasets/PPMI_T1_3D_PDOnly', '/mnt/e/ShareFolder/Datasets/PDOnly_JPG')