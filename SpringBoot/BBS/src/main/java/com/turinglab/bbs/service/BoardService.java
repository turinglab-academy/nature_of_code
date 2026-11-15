package Service;

import Entity.Board;
import Repository.BoardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class BoardService {
    private final BoardRepository boardRepository;

    public List<Board> boardList() {
        return boardRepository.findAll();
    }

    public void write(Board board) {
        boardRepository.save(board);
    }
}
