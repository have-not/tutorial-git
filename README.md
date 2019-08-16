# tutorial-git
## 使い方練習  
### 開発してコミットしてプルリクする  
   1. web操作で自分のリポジトリにフォークする  
   1. 自分のリポジトリからクローンする  

          git clone { 自分のリポジトリ }/tutorial-git.git

   1. クローンしたフォルダに自分のフォルダを作る  

          cd tutorial-git
          mkdir $USER

   1. なにかつくる  

          cd ./$USER
          echo "I made my dir" >> README.md

   1. `commit`,`push`する  

          cd ..
          git add ./$USER
          git commit -m "ADD my develop dir"
          git push origin master

   1. プルリクエストを送る  
      1. もし**2回以上コミットしている**なら、コミットを`rabase`で`squash`する  
         1. 例：5回コミットしている時  

                git rebase -i HEAD~5

         1. 2行目以降の`pick`を`squash`に変更し、保存する  
         1. 再度出る画面で（コメントを修正したければ修正し）保存する  
         1. 変更内容を強制`push`する  
            失敗する場合は、[Projects]->[対象project]->[Settings]->[Protected branches]->[Unprotectedボタン]で解除

                git push -f origin master

      1. web操作でプルリクする  

### フォーク元ブランチを追いかける  
   1. フォーク後、フォーク元を更新してもらう  
   1. フォーク元リポジトリの更新を取り込む  

          git remote add upstream { 元のブランチ }/tutorial-git.git
          git fetch upstream
          git marge upstream/master
