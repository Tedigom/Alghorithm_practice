//
//  DataModel.swift
//  Demo
//
//  Created by mac on 2018. 2. 9..
//  Copyright © 2018년 Seong ho Hong. All rights reserved.
//

import Foundation
import UIKit
import THContentMarkerView
import Firebase
import FirebaseDatabase
import Kingfisher

class DataModel {
    var markerArray = [THMarker]()
    var thumbnailURL = [URL]()
    var refer: DatabaseReference!
    var imgKey = [String]()
    var imgPath = "imghash1"
    var getData = [String:Any]()

func setup() {
        refer = Database.database().reference()
    }
    func getSnapshot(completionHandler:@escaping (Bool) -> ()) {
        refer.observeSingleEvent(of: .value, with: { (snapshot) in
                                 if let getData = snapshot.value as? [String:Any] {
                                 self.getData = getData
                                 }
                                 completionHandler(true)
                                 })
}

func getImgs() {
        let imgs = getData.keys.sorted()
        for img in imgs {
            if let imgData = getData[img] as? [String:Any] {
                imgKey.append(img)
                if let thumbnail = imgData["thumbnail"] as? String {
                    let url = URL(string: thumbnail)
                    thumbnailURL.append(url!)
            }
        }
}
    }
    func getTileImageBaseURL() -> URL {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let tileImageBaseURL = imgData["img"] as? String {
                print(getTileImageName())
                return URL(string: "http://172.30.1.37:5000/" + getTileImageName())!
            
            } else {
                return URL(string: "http://172.30.1.37:5000/")!
    }
        } else {
            
            return URL(string: "http://172.30.1.37:5000/")!
}
    }
    func getTileImageName() -> String {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let tileImageName = imgData["imgName"] as? String {
                return tileImageName
            } else {
                return ""
        }
        } else {
            return ""
}
    }
    func getTileImageExtension() -> String {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let tileImageExtension = imgData["imgExtension"] as? String {
                return tileImageExtension
            } else {
                return "jpg"
        }
        } else {
            return "jpg"
}
    }
    func getImgSize() -> CGSize? {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let width = imgData["width"] as? Float, let height = imgData["height"] as? Float {
                return CGSize(width: CGFloat(width), height: CGFloat(height))
            } else {
                return nil
        }
        } else {
            return nil
}
    }
    func getMaxTileLevel() -> Int {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let maxTileLevel = imgData["maxTileLevel"] as? Int {
                return maxTileLevel
            } else {
                return 3
        }
        } else {
            return 3
}
    }
    func getMinTileLevel() -> Int {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let minTileLevel = imgData["minTileLevel"] as? Int {
                return minTileLevel
            } else {
                return 1
        }
        } else {
            return 1
}
    }
    func getMaxZoomLevel() -> Float {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let maxZoomLevel = imgData["maxTileLevel"] as? Float {
                return maxZoomLevel
            } else {
                return 8
        }
        } else {
            return 8
}
    }
    func getTileSizeArray() -> [CGSize] {
        var tileSize = [CGSize]()
        let maxLevel = self.getMaxTileLevel()
        let minLevel = self.getMinTileLevel()
        if let imgData = getData[imgPath] as? [String:Any] {
            if let tile = imgData["tile"] as? [String:Any] {
                for index in minLevel...maxLevel {
                    if let length = tile["level"+index.description] as? Int {
                        let size = CGSize(width: length, height: length)
                        print(size)
                        tileSize.append(size)
                }
            }
    }
        }
        if tileSize.isEmpty {
            for _ in minLevel...maxLevel {
                tileSize.append(CGSize(width:10000, height:10000))
        }
        }
        return tileSize
}
    func getMarkers(scrollView: UIScrollView) {
        if let imgData = getData[imgPath] as? [String:Any] {
            if let markers = imgData["markers"] as? [String:Any] {
                self.markerArray.removeAll()
                let markerKeyArray = markers.keys.sorted()
                let markerNum = markers.count
                for i in 0..<markerNum {
                    let markerInfo = markers[markerKeyArray[i]] as! [String:Any]
                    let position = markerInfo["position"] as! [String: Float]
                    let x = position["x"]
                    let y = position["y"]
                    let zoomScale = position["zoomScale"]
                    var content = [String: Any]()
                    if let contents = markerInfo["contents"] as? [String: Any] {
                        if let title = contents["title"] as? String {
                            if title != "" {
                                content["titleContent"] = title
                        }
                        }
                        if let video = contents["video"] as? String {
                            if video != "" {
                                content["videoContent"] = URL(string: video)
                        }
                        }
                        if let audio = contents["audio"] as? String {
                            if audio != "" {
                                content["audioContent"] = URL(string: audio)
                        }
                        }
                        var textContent = [String: String]()
                        if let textTitle = contents["textTitle"] as? String {
                            if textTitle != "" {
                                textContent["title"] = textTitle
                        }
                        }
                        if let link = contents["link"] as? String {
                            if link != "" {
                                textContent["link"] = link
                        }
                        }
                        if let text = contents["text"] as? String {
                            if text != "" {
                                textContent["text"] = text
                        }
                        }
                        if textContent != [String: String]() {
                            content["textContent"] = textContent
        }
            }
                let marker = THMarker(zoomScale: CGFloat(zoomScale!) , origin: CGPoint(x: CGFloat(x!), y: CGFloat(y!)), markerID: markerKeyArray[i], contentInfo: content)
                self.markerArray.append(marker)
            }
        }
    }
}
    func getMarkers(scrollView: UIScrollView, completionHandler:@escaping (Bool) -> ()) {
        refer.child(imgPath).child("markers").observeSingleEvent(of: .value, with: { (snapshot) in
                                                                 if let markers = snapshot.value as? [String:Any] {
                                                                 self.markerArray.removeAll()
                                                                 let markerKeyArray = markers.keys.sorted()
                                                                 let markerNum = markers.count
                                                                 for i in 0..<markerNum {
                                                                 let markerInfo = markers[markerKeyArray[i]] as! [String:Any]
                                                                 let position = markerInfo["position"] as! [String: Float]
                                                                 let x = position["x"]
                                                                 let y = position["y"]
                                                                 let zoomScale = position["zoomScale"]
                                                                 var content = [String:Any]()
                                                                 if let contents = markerInfo["contents"] as? [String: Any] {
                                                                 if let title = contents["title"] as? String {
                                                                 if title != "" {
                                                                 content["titleContent"] = title
                                                                 }
                                                                 }
                                                                 if let video = contents["video"] as? String {
                                                                 if video != "" {
                                                                 content["videoContent"] = URL(string: video)
                                                                 }
                                                                 }
                                                                 if let audio = contents["audio"] as? String {
                                                                 if audio != "" {
                                                                 content["audioContent"] = URL(string: audio)
                                                                 }
                                                                 }
                                                                 var textContent = [String: String]()
                                                                 if let textTitle = contents["textTitle"] as? String {
                                                                 if textTitle != "" {
                                                                 textContent["title"] = textTitle
                                                                 }
                                                                 }
                                                                 if let link = contents["link"] as? String {
                                                                 if link != "" {
                                                                 textContent["link"] = link
                                                                 }
                                                                 }
                                                                 if let text = contents["text"] as? String {
                                                                 if text != "" {
                                                                 textContent["text"] = text
                                                                 }
                                                                 }
                                                                 if textContent != [String: String]() {
                                                                 content["textContent"] = textContent
                                                                 }
                                                                 }
                                                                 let marker = THMarker(zoomScale: CGFloat(zoomScale!) , origin: CGPoint(x: CGFloat(x!), y: CGFloat(y!)), markerID: markerKeyArray[i], contentInfo: content)
                                                                 self.markerArray.append(marker)
                                                                 }
                                                                 }
                                                                 completionHandler(true)
                                                                 })
    }
    func addMarker(position: [String: Float], contents: [String: String], markerID: String) {
        let markerInfo = ["position":position, "contents":contents] as [String : Any]
        self.refer.child(self.imgPath).child("markers").child(markerID).setValue(markerInfo)
        if var imgData = getData[imgPath] as? [String:Any] {
            if var markers = imgData["markers"] as? [String:Any] {
                markers[markerID] = markerInfo
                imgData.updateValue(markers, forKey: "markers")
                getData.updateValue(imgData, forKey: imgPath)
        }
    }
}
    func deleteMarker(markerID: String) {
        self.refer.child(self.imgPath).child("markers").child(markerID).removeValue()
        if var imgData = getData[imgPath] as? [String:Any] {
            if var markers = imgData["markers"] as? [String:Any] {
                markers.removeValue(forKey: markerID)
                imgData.updateValue(markers, forKey: "markers")
                getData.updateValue(imgData, forKey: imgPath)
        }
    }
}
}
