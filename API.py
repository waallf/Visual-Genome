from visual_genome import local
path = "C:\\Users\Administrator\Desktop\视觉基因数据集\\"
'''
[[id,x,y,width,height,phrase,id,x,y,width,height,phrase],[id1,x,y,width,height,phrase,..]]
'''
# s = local.get_all_region_descriptions(path)

'''
start_index :读取图片的开始索引
end_index ：读取图片的结束索引
data_dir ：根目录
image_data_dir:by-id 目录
min_rels ：将relationships限制在  min_rels，max_rels
max_rels

return：list 

list[0].attributes:<class 'list'>: []
list[0].image:id: 1, coco_id: -1, flickr_id: -1, width: 800, url: https://cs.stanford.edu/people/rak248/VG_100K_2/1.jpg
list[0].object:<class 'list'>: [clock, street, shade, man, sneakers, headlight, car, bike, bike, sign, building, tree trunk, sidewalk, shirt, street, car, back, glasses, parking meter, shoes, man, pants, jacket, pants, work truck, sidewalk, chin, guy, van, wall, tree, bikes, arm, shirt, man, man, road, lamp post, trees, windows]
list[0].relationships:<class 'list'>: <class 'list'>: [15927: shade ON street, 15928: man wears sneakers, 15929: car has headlight, 15930: sign ON building, 15931: tree trunk ON sidewalk, 15932: man has shirt, 15933: sidewalk next to street, 15934: car has back, 15935: man has glasses, 15936: parking meter ON sidewalk, 15937: man wears sneakers, 15938: man has shoes, 15939: man has shirt, 15940: man wears pants, 15941: man has jacket, 15942: man has pants, 15943: bike parked on sidewalk, 15944: bike parked on sidewalk, 15945: work truck parked on street, 15946: car parked on street, 4265923: bike ON sidewalk, 3186256: parking meter behind man, 3186257: guy holding chin, 3186258: man WEARING shirt, 3186259: man holding chin, 3186260: bikes near tree, 3186261: man WEARING shoes, 3186262: bikes near tree, 3186263: shirt ON man, 4265924: man holding chin, 4265925: man WEARING glasses, 4265926: lamp post along road, 3186264: man IN shirt, 3186265: man WEARING pants, 3186266: parking meter on top of street, 3186267: tree next to street, 3186268: man WEARING glasses, 3186269: bikes behind man, 3186270: trees by sidewalk, 3186271: man WEARING jacket, 4265927: building with windows]

'''
# local.save_scene_graphs_by_id(path,image_data_dir=path+"/by-id")#先按image id将scene_graphs存储
# scene_graph = local.get_scene_graphs(start_index = 0,end_index = 10,data_dir = path,
#                                      image_data_dir = path+"/by-id/",min_rels=0,max_rels=100)

